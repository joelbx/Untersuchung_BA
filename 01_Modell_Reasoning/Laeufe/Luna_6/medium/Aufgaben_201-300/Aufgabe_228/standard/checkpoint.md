# Version parsing issue checkpoint

- Inspect existing Qt bindings, version decisions, and targeted tests.
- Add `utils.parse_version` backed by `QVersionNumber` and migrate the requested call sites.
- Run the relevant existing tests and review the final diff.
