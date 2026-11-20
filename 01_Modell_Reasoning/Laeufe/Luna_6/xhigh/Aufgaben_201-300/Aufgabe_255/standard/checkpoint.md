# Password lookup fix checkpoint

- Objective: fix parsing of password lookup `key=value` parameters, including option defaults, character specifications, and deterministic seeds.
- Constraints: use repository code and existing tests only; do not alter git history, index baseline, or harness configuration.
- Implementation: moved `_parse_parameters` onto `LookupModule`, loaded options before parsing, applied term-over-option precedence, rejected unknown keys, and declared `chars` as a raw option with the required default list.
- Character handling: comma-separated strings split only when the input is a string; doubled commas become literal comma characters; list inputs remain unchanged.
- Coverage: existing password lookup unit tests plus cases for deterministic inline seeds and both option value forms passed: 33 passed.
- Review: `git diff --check` passed; only the plugin and its unit test file are modified.
- Status: complete.
