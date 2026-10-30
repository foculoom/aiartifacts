"""Behavioral checks for the portable editorial warning checker."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "prose_lint.py"
SPEC = importlib.util.spec_from_file_location("prose_lint", SCRIPT)
lint = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = lint
SPEC.loader.exec_module(lint)

PARAGRAPH = (
    "The customer opened the report and checked each total against the "
    "original invoice before sending a short explanation to the support "
    "team with the specific correction that was needed."
)


class ProseTests(unittest.TestCase):
    def scan(self, text, **kwargs):
        return lint.lint_documents({"draft.md": text}, **kwargs)

    def test_exact_word_boundaries_and_case(self):
        safe = ("gateway gatekeeper tranches delved tapestrywork "
                "testamentary beacons revolutionized moreoverish "
                "furthermorex gate_id αgate gateβ")
        self.assertEqual(self.scan(safe), [])
        found = self.scan("GATE. Delve! gate's latch.")
        self.assertEqual(len(found), 1)  # one candidate per rule/line/excerpt
        self.assertEqual(found[0].rule, "word-choice")
        self.assertEqual(found[0].line, 1)

    def test_long_line_excerpt_includes_the_flagged_word(self):
        text = "Opening context. " + "ordinary words " * 50
        text += "beacon " + "later context " * 50
        found = self.scan(text)
        self.assertEqual(len(found), 1)
        self.assertIn("beacon", found[0].excerpt)
        self.assertNotIn("Opening context", found[0].excerpt)
        self.assertLessEqual(len(found[0].excerpt), 160)
        self.assertEqual(found[0].line, 1)

    def test_each_requested_word_is_detected(self):
        found = self.scan("\n".join(lint.TERMS))
        self.assertEqual(len(found), 9)
        self.assertEqual([item.line for item in found], list(range(1, 10)))

    def test_stock_phrases_apostrophes_whitespace_and_boundaries(self):
        text = ("In today’s fast‑paced world we wait.\n"
                "It is\nworth noting this fact.\n"
                "In conclusion, stop.\nTo summarize, read.\n"
                "Notin conclusionary prose.")
        found = [item for item in self.scan(text) if item.rule == "stock-phrase"]
        self.assertEqual([item.line for item in found], [1, 2, 4, 5])

    def test_allow_terms_are_exact_case_insensitive_and_repeatable(self):
        found = self.scan("Gate and beacon.\nIn conclusion, stop.\nDelve.",
                          allow_terms=[" GATE ", "beacon", "IN CONCLUSION"])
        self.assertEqual([(item.line, item.rule) for item in found],
                         [(3, "word-choice")])
        self.assertEqual(len(self.scan("gate", allow_terms=["gateway"])), 1)

    def test_frontmatter_comments_quotes_and_source_lines(self):
        text = ("---\ntitle: delve\ntags: [gate]\n---\n"
                "<!-- beacon\nmoreover -->\n"
                "> tapestry is a quotation.\n"
                "This lazy continuation says furthermore.\n\n"
                "Ordinary gate prose.\n")
        found = self.scan(text)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].line, 10)
        self.assertEqual(found[0].excerpt, "Ordinary gate prose.")
        self.assertEqual(lint.visible_prose(text).count("\n"), text.count("\n"))

    def test_bom_and_alternate_yaml_end(self):
        self.assertEqual(self.scan("\ufeff---\ntitle: delve\n...\nClear prose."), [])
        found = self.scan("---\ntitle: delve\nunterminated metadata")
        self.assertEqual([(item.line, item.rule) for item in found],
                         [(2, "word-choice")])

    def test_fences_support_tildes_lengths_and_matching_character(self):
        text = ("````python\ndelve\n```\nbeacon\n~~~~\ngate\n`````\n"
                "~~~text\nmoreover\n~~~~\nVisible testament.\n")
        found = self.scan(text)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].line, 11)
        self.assertIn("testament", found[0].excerpt)

    def test_unclosed_fence_is_not_prose(self):
        self.assertEqual(self.scan("Before.\n~~~\ndelve\nbeacon"), [])

    def test_inline_code_exact_runs_and_multiline(self):
        text = ("A `delve` example and ``a ` gate`` sample.\n"
                "A `beacon\nmoreover` example.\nVisible tapestry.")
        found = self.scan(text)
        self.assertEqual([(item.line, item.rule) for item in found],
                         [(4, "word-choice")])

    def test_unmatched_code_does_not_hide_later_paragraph(self):
        found = self.scan("An unmatched ` mark.\n\nA gate.\n\n`beacon`.")
        self.assertEqual([(item.line, item.rule) for item in found],
                         [(3, "word-choice")])

    def test_comment_markers_inside_code_do_not_swallow_prose(self):
        text = ("```html\n<!-- not a prose comment\n```\n"
                "A gate.\n`<!-- still code`\nA beacon.\n"
                "<!--\n```\ndelve\n-->\nA testament.")
        self.assertEqual([item.line for item in self.scan(text)], [4, 6, 11])

    def test_links_keep_labels_but_not_destinations_or_titles(self):
        text = ("[beacon](relative/gate.md \"delve\")\n"
                "[read](docs/a(gate).md 'tapestry')\n"
                "[moreover][gate]\n[gate]: https://example.test/delve\n"
                "https://example.test/tranche www.example.test/beacon\n"
                "<https://example.test/testament>\n")
        found = self.scan(text)
        self.assertEqual([item.line for item in found], [1, 3])
        self.assertIn("beacon", found[0].excerpt)
        self.assertNotIn("relative", found[0].excerpt)

    def test_blockquote_ends_at_unquoted_heading(self):
        found = self.scan("> gate\n## New section\nVisible beacon.\n")
        self.assertEqual([item.line for item in found], [3])

    def test_blank_quoted_line_ends_lazy_continuation(self):
        found = self.scan("> quoted gate\n> \nVisible beacon.\n")
        self.assertEqual([item.line for item in found], [3])

    def test_repeated_substantive_paragraph_across_documents(self):
        docs = {"one.md": "# One\n\n" + PARAGRAPH,
                "two.txt": "\n" + PARAGRAPH.replace(" ", "\n", 3),
                "three.md": "short repeated text\n\nshort repeated text"}
        found = lint.lint_documents(docs)
        repeated = [item for item in found if item.rule == "repeated-paragraph"]
        self.assertEqual([(item.path, item.line) for item in repeated],
                         [("one.md", 3), ("two.txt", 2)])

    def test_short_or_same_document_repeat_is_not_cross_input_finding(self):
        self.assertEqual(self.scan(PARAGRAPH + "\n\n" + PARAGRAPH), [])
        self.assertEqual(lint.lint_documents({"a.md": "only three words",
                                              "b.md": "only three words"}), [])

    def test_masked_repeated_paragraphs_do_not_count(self):
        self.assertEqual(lint.lint_documents({
            "a.md": PARAGRAPH,
            "b.md": "~~~\n" + PARAGRAPH + "\n~~~",
            "c.md": "> " + PARAGRAPH,
        }), [])

    def test_repeated_h2_check_is_optional_and_has_thresholds(self):
        headings = "\n\n".join("## " + name for name in
                                   ["Practice", "Questions", "Review", "Explain"])
        docs = {f"{i}.md": "# Unique " + str(i) + "\n\n" + headings
                for i in range(3)}
        self.assertEqual(lint.lint_documents(docs), [])
        found = lint.lint_documents(docs, check_heading_sequences=True)
        self.assertEqual(len(found), 3)
        self.assertTrue(all(item.rule == "repeated-h2-sequence" for item in found))
        self.assertEqual(lint.lint_documents(dict(list(docs.items())[:2]),
                         check_heading_sequences=True), [])
        three = {key: value.rsplit("\n\n", 1)[0] for key, value in docs.items()}
        self.assertEqual(lint.lint_documents(three, check_heading_sequences=True), [])

    def test_only_longest_qualifying_heading_suffix_is_reported(self):
        text = "\n".join(f"## Section {number}" for number in range(6))
        found = lint.lint_documents({f"{i}.md": text for i in range(3)},
                                   check_heading_sequences=True)
        self.assertEqual(len(found), 3)
        self.assertTrue(all(item.line == 1 for item in found))


class FilesAndCliTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="prose-lint-")
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def write(self, relative, text="Clear writing."):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              text=True, capture_output=True, check=False)

    def test_discovery_filters_types_generated_dirs_and_duplicate_inputs(self):
        first = self.write("chapter.md", "gate")
        second = self.write("nested/notes.TXT", "beacon")
        self.write("manual.pdf", "delve")
        for folder in [".git", ".agents", ".codex", "node_modules",
                       "venv", ".venv", "build", "dist", "target", ".cache"]:
            self.write(folder + "/ignored.md", "delve")
        self.assertEqual(lint.collect_paths([self.root, first]),
                         sorted([first, second], key=str))
        self.assertEqual(lint.collect_paths([self.root / "build"]), [])

    def test_symlinks_are_skipped_and_explicit_links_rejected(self):
        target = self.write("real.md", "gate")
        link = self.root / "linked.md"
        directory = self.root / "linked-dir"
        try:
            link.symlink_to(target)
            directory.symlink_to(self.root, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable on this platform")
        self.assertEqual(lint.collect_paths([self.root]), [target])
        with self.assertRaises(lint.LintError):
            lint.collect_paths([link])
        with self.assertRaises(lint.LintError):
            lint.collect_paths([directory / "real.md"])

    def test_default_success_and_explicit_strict_failure(self):
        path = self.write("draft.md", "A gate.")
        ordinary = self.cli(path)
        strict = self.cli(path, "--fail-on-findings")
        self.assertEqual(ordinary.returncode, 0)
        self.assertIn("review candidate", ordinary.stdout)
        self.assertEqual(strict.returncode, 1)
        self.assertEqual(self.cli(path, "--allow-term", "gate",
                                  "--fail-on-findings").returncode, 0)

    def test_json_contract_and_repeatable_allow_option(self):
        path = self.write("draft.txt", "gate and beacon\nMoreover.")
        result = self.cli(path, "--format", "json", "--allow-term", "gate",
                          "--allow-term", "beacon")
        self.assertEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertEqual(set(payload), {"files_checked", "findings"})
        self.assertEqual(payload["files_checked"], 1)
        self.assertEqual(len(payload["findings"]), 1)
        self.assertEqual(set(payload["findings"][0]),
                         {"path", "line", "rule", "excerpt"})
        self.assertEqual(payload["findings"][0]["line"], 2)

    def test_clean_and_empty_directories_return_zero_without_quality_claim(self):
        path = self.write("clean.md")
        result = self.cli(path, "--fail-on-findings")
        self.assertEqual(result.returncode, 0)
        self.assertIn("not a quality assessment", result.stdout)
        empty = self.root / "empty"
        empty.mkdir()
        result = self.cli(empty, "--format", "json")
        self.assertEqual(json.loads(result.stdout), {"files_checked": 0, "findings": []})

    def test_missing_unsupported_invalid_utf8_and_usage_exit_two(self):
        unsupported = self.write("file.docx")
        invalid = self.root / "invalid.md"
        invalid.write_bytes(b"\xff\xfe")
        for args in [(self.root / "missing.md",), (unsupported,), (invalid,),
                     (), (self.root, "--format", "xml")]:
            with self.subTest(args=args):
                result = self.cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertTrue(result.stderr)
                self.assertEqual(result.stdout, "")

    def test_cli_does_not_rewrite_source(self):
        path = self.write("draft.md", "# Draft\n\nMoreover, a gate.")
        before = path.read_bytes()
        self.cli(path, "--fail-on-findings")
        self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
