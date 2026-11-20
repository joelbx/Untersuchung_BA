Task: Add Path and typed-list support to FnToCLI, explicit option mapping, parse_args(args), and run return values.
Status: Complete. Updated implementation and tests; 12 FnToCLI tests pass, Ruff and git diff --check pass.
Decisions: Required lists are positional; optional lists use flags and default to None when omitted. Underscore option spelling is accepted directly; existing dashed spelling remains available and displayed in usage.
Delegation: None; solved in coordinator worktree.
