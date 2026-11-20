# Checkpoint

Task: Resolve the incomplete `:buffer` to `:tab-select` rename across commands, completion, and help/configuration references.

Completed:
- Renamed the registered command to `tab-select` and retained index matching, count precedence, cross-window focus, and `qute://tabs` behavior.
- Renamed tab completion sources to `tabs` and `other_tabs`, and updated `tab-take` to use the new provider.
- Updated the default `gt` binding, regenerated command/settings help, and renamed relevant unit/end-to-end scenario references.
- Verified no stale `:buffer` command/provider references remain in the active command, help, config, or targeted test files.

Verification:
- `python3 -m pytest tests/unit/completion/test_models.py tests/unit/completion/test_completer.py`: 154 passed, 1 xfailed.
- `python3 -m pytest tests/unit/completion/test_models.py -k 'tab_completion or other_tabs' -q`: 5 passed.
- End-to-end tab/completion run could not start its browser process in this environment; startup reports unavailable QtWebKit and exits before scenarios run.
- `python3 scripts/dev/src2asciidoc.py` and `git diff --check` completed successfully.
