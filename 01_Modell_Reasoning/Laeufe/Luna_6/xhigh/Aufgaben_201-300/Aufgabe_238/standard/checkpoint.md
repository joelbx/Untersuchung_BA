# Checkpoint

Task: complete the `:buffer` to `:tab-select` rename across command registration, tab completion providers, current help, configuration examples, and existing references/tests.

Status: implementation and generated documentation are updated. `tab_select` retains numeric and title/URL matching, count precedence, cross-window IDs, focus behavior, and the no-argument tabs page. Completion providers are `tabs` and `other_tabs`; the default `gt` binding now opens `:tab-select`.

Validation:
- `python3 scripts/dev/src2asciidoc.py` completed and generated the updated command/settings help.
- `xvfb-run ... pytest tests/unit/completion/test_models.py -q`: 73 passed.
- Focused tab-select and completion end-to-end scenarios with Chromium's root sandbox flag: 13 passed, 1 skipped.
- `git diff --check` passed. Active `:buffer`/old completion-provider references were absent outside the historical changelog.
- `check_doc_changes.py` reported the expected modified generated docs in the working tree.
