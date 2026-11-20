# Work checkpoint

Issue: Support module deprecations by date while preserving version deprecation behavior.

Implemented:
- Python warning collection, `AnsibleModule.deprecate`, `exit_json` normalization, removed-at-date option metadata, and deprecated alias validation/recording.
- C# `DateTime` overload, date-based option/alias handling, and date validation.
- `Display.deprecated` renders returned date deprecations; validate-modules schema and checks recognize date metadata.
- Updated module deprecation documentation and the existing Windows test expectation affected by new metadata/error text.

Validation:
- Focused Python unit suites passed: 96 passed using `pytest --forked`.
- Direct `AnsibleModule.exit_json()` smoke check passed for date formatting, assertion text, entry shapes, and merge order.
- Python compile checks and `git diff --check` passed.
- Runtime validate-modules schema check could not run because `voluptuous` is unavailable. Windows integration tests are unavailable in this Linux environment.
