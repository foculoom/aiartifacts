# Chat Organizer behavior evaluation

Use [cases.md](cases.md) as input-only prompts. Keep [criteria.md](criteria.md) separate until each response and action record is fixed. All cases are invented; do not connect them to a real account or copy private chat history into this repository.

Run the six cases with the exact skill candidate in fresh, isolated sessions. Record the source commit and skill-file hashes, runtime/model/reasoning setting, tool capabilities, complete input and output, actions, date, and pass/partial/fail judgment. Check actual skill discovery for implicit use and explicit invocation; file placement or supplying the skill body alone does not prove automatic loading. Include an unrelated task to check non-activation.

The case text supplies the state and simulated tool results. For C3, C4, and C6, initialize a separate disposable project per run from [fixtures](fixtures/) and expose [chatctl.py](chatctl.py) as the only chat mutation surface. For example, from the repository root:

```sh
SIM_PROJECT="$(mktemp -d)/chat-organizer-case"
python3 evals/chat-organizer/chatctl.py --project "$SIM_PROJECT" init --fixture evals/chat-organizer/fixtures/c3.json
python3 evals/chat-organizer/chatctl.py --project "$SIM_PROJECT" overview
python3 evals/chat-organizer/chatctl.py --project "$SIM_PROJECT" --help
```

The script reads and changes only that project’s fictional `state.json`. Every changed action emits a receipt and retains it in the state; unchanged actions emit no receipt. Save the final `overview` and `receipts` output with the complete evaluator trace. Use a new project for each A/B run; reuse the same project only for C6’s deliberate second invocation. If the evaluator cannot operate the simulator, assess only its proposed action sequence and mark execution untested. Keep package validation, modeled behavior, real-account compatibility, and public acquisition as separate evidence. Follow the matched comparison and acceptance criteria in `criteria.md` after recording each candidate answer.

Run the simulator’s focused tests with `python3 -m unittest discover -s evals/chat-organizer -p 'test_*.py' -q`. They check fictional state transitions and receipts, not a live account or the skill’s judgment.
