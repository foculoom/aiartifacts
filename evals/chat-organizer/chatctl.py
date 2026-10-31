#!/usr/bin/env python3
"""Operate a disposable, fictional chat workspace for behavior evaluations."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys


def output(value):
    print(json.dumps(value, ensure_ascii=False, sort_keys=True))


def fail(code, detail):
    output({"ok": False, "code": code, "detail": detail})
    return 2


def load(project):
    path = project / "state.json"
    if not path.is_file() or path.is_symlink():
        raise ValueError("missing or linked state.json; initialize a disposable project first")
    return json.loads(path.read_text(encoding="utf-8"))


def save(project, state):
    path = project / "state.json"
    temporary = project / "state.json.next"
    if temporary.exists() or temporary.is_symlink():
        raise ValueError("temporary state already exists")
    try:
        with temporary.open("x", encoding="utf-8") as target:
            json.dump(state, target, ensure_ascii=False, indent=2, sort_keys=True)
            target.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def find(items, identifier):
    return next((item for item in items if item["id"] == identifier), None)


def update(project, state, operation, identifier, before, after):
    if before == after:
        return {"ok": True, "changed": False, "id": identifier, "state": after}
    receipt = {
        "at": datetime.now(timezone.utc).isoformat(),
        "operation": operation,
        "id": identifier,
        "before": before,
        "after": after,
    }
    state.setdefault("receipts", []).append(receipt)
    save(project, state)
    return {"ok": True, "changed": True, "receipt": receipt}


def parser():
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--project", required=True, type=Path, help="disposable project directory")
    commands = root.add_subparsers(dest="command", required=True)
    initialize = commands.add_parser("init", help="copy a fictional fixture into a new project")
    initialize.add_argument("--fixture", required=True, type=Path)
    commands.add_parser("overview", help="read chats, projects, sections, and automations")
    show = commands.add_parser("show", help="read one chat by stable ID")
    show.add_argument("--id", required=True)
    context = commands.add_parser("project-context", help="read one destination context")
    context.add_argument("--id", required=True)
    commands.add_parser("receipts", help="read actions recorded in this project")
    move = commands.add_parser("move", help="move one active chat to a compatible private project")
    move.add_argument("--id", required=True)
    move.add_argument("--project-id", required=True)
    archive = commands.add_parser("set-archive", help="set archive state")
    archive.add_argument("--id", required=True)
    archive.add_argument("--value", choices=("true", "false"), required=True)
    rename = commands.add_parser("rename", help="set a chat title")
    rename.add_argument("--id", required=True)
    rename.add_argument("--title", required=True)
    pin = commands.add_parser("set-pin", help="set pin state")
    pin.add_argument("--id", required=True)
    pin.add_argument("--value", choices=("true", "false"), required=True)
    section = commands.add_parser("ensure-section", help="reuse or create a sidebar section")
    section.add_argument("--name", required=True)
    placement = commands.add_parser("set-section", help="move one chat into an existing section")
    placement.add_argument("--id", required=True)
    placement.add_argument("--name", required=True)
    return root


def main(argv=None):
    args = parser().parse_args(argv)
    project = args.project.resolve()
    if args.command == "init":
        if project.exists() and (not project.is_dir() or any(project.iterdir())):
            return fail("PROJECT_NOT_EMPTY", "use a new empty directory")
        fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
        if not all(key in fixture for key in ("chats", "projects", "sections", "automations")):
            return fail("INVALID_FIXTURE", "fixture lacks required collections")
        project.mkdir(parents=True, exist_ok=True)
        save(project, fixture)
        output({"ok": True, "project": str(project), "case": fixture.get("case")})
        return 0
    try:
        state = load(project)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        return fail("STATE_UNAVAILABLE", str(error))

    if args.command == "overview":
        output({"ok": True, **state})
        return 0
    if args.command == "receipts":
        output({"ok": True, "receipts": state.get("receipts", [])})
        return 0
    if args.command == "project-context":
        item = find(state["projects"], args.id)
        if item is None:
            return fail("UNKNOWN_PROJECT", args.id)
        output({"ok": True, "project": item})
        return 0
    if args.command == "ensure-section":
        if not args.name.strip():
            return fail("EMPTY_SECTION", "name required")
        if args.name in state["sections"]:
            output({"ok": True, "changed": False, "name": args.name})
            return 0
        before = list(state["sections"])
        state["sections"].append(args.name)
        output(update(project, state, "ensure-section", args.name, before, list(state["sections"])))
        return 0

    chat = find(state["chats"], args.id)
    if chat is None:
        return fail("UNKNOWN_CHAT", args.id)
    if args.command == "show":
        output({"ok": True, "chat": chat})
        return 0

    before = dict(chat)
    if args.command == "move":
        destination = find(state["projects"], args.project_id)
        if destination is None:
            return fail("UNKNOWN_PROJECT", args.project_id)
        if chat["archived"] and chat["project_id"] != args.project_id:
            return fail("ARCHIVED_MOVE_UNSUPPORTED", "restore chat before changing membership")
        if destination["sharing"] != "owner-only" and chat["project_id"] != args.project_id:
            return fail("SHARED_BOUNDARY", "destination has collaborators")
        if chat.get("kind") == "work" and destination["memory"] == "project-only" and chat["project_id"] != args.project_id:
            return fail("MEMORY_INCOMPATIBLE", "Work conversation cannot enter project-only memory")
        chat["project_id"] = args.project_id
        operation = "move"
    elif args.command == "set-archive":
        chat["archived"] = args.value == "true"
        operation = "set-archive"
    elif args.command == "rename":
        if not args.title.strip():
            return fail("EMPTY_TITLE", "title required")
        chat["title"] = args.title
        operation = "rename"
    elif args.command == "set-pin":
        chat["pinned"] = args.value == "true"
        operation = "set-pin"
    elif args.command == "set-section":
        if args.name not in state["sections"]:
            return fail("UNKNOWN_SECTION", args.name)
        chat["section"] = args.name
        operation = "set-section"
    else:
        return fail("UNKNOWN_COMMAND", args.command)
    output(update(project, state, operation, args.id, before, dict(chat)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
