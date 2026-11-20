The failure starts at [`later(ms: int, …)`](/app/qutebrowser/misc/utilcmds.py:45): command argument conversion rejects `5s` before the handler runs. [`utils.py`](/app/qutebrowser/utils/utils.py:248) has no `parse_duration`.

The fix should add a parser that accepts full `h`, `m`, and `s` expressions with decimal components, sums them into integer milliseconds, preserves digit-only input as milliseconds, and raises `ValueError` for empty, negative, or malformed input. `later` should accept a string, call the parser, and turn invalid input into a command error before setting the timer.

One boundary needs a decision: the command runner’s `maxsplit=1` treats whitespace after the first duration token as part of the target command, so the parser can allow `2m 15s` while `:later 2m 15s …` will not pass that whole expression to it. Existing `:later` coverage is in [`utilcmds.feature`](/app/tests/end2end/features/utilcmds.feature:9); parser cases belong in [`test_utils.py`](/app/tests/unit/utils/test_utils.py:1).

I recorded the diagnosis in [checkpoint.md](/app/.codex-role-output/checkpoint.md). Source and tests were not edited or run because this run was restricted to fault localization.