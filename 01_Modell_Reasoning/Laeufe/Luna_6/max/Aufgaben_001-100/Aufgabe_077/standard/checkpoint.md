# Work checkpoint

Issue: Support module deprecation dates across Python warnings/AnsibleModule, deprecated alias validation, schema/display behavior, and the C# module API.

Initial state: `/app` has no reported tracked or untracked changes; `.codex-role-output/` was empty.

Plan: inspect repository guidance and affected code/tests, implement the required behavior, then run relevant existing test suites.

Findings: Python global deprecations are accumulated in call order. Explicit `exit_json` deprecations are appended, but mapping entries currently discard `date`. Parameter scanning only recognizes `removed_in_version`; callback display accepts only `version`. PowerShell validation wraps argument-spec errors as `internal error:` and currently requires `version` on each deprecated alias.

Implementation: added date-shaped warning records, Python `AnsibleModule.deprecate` date support and conflict assertion, ordered `exit_json` mapping date handling, `removed_at_date` parameter scanning, date-aware display, validate-modules date schema/expiry checks, and C# `DateTime` overload/alias validation. Updated existing PowerShell assertions for the new metadata key and required one-of error.

Verification: 116 relevant existing Python unit tests passed with pytest fork isolation; Python bytecode compilation passed; `git diff --check` passed. The validate-modules sanity runner could not start because `voluptuous` is not installed. C# integration tests could not run because `pwsh` and C# compilers are unavailable.
