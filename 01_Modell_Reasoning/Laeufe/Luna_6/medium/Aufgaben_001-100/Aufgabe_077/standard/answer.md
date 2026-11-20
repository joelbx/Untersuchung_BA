Implemented date based deprecations across Python warnings, `AnsibleModule`, argument handling, validate-modules, and the C# `DateTime` overload.

`git diff --check` passed. Focused pytest runs had failures because warning and deprecation globals accumulate across test cases; several failures showed prior test entries in later results. The parameter and argument-spec checks otherwise passed. I did not run C# tests.

The required checkpoint is at `.codex-role-output/checkpoint.md`.