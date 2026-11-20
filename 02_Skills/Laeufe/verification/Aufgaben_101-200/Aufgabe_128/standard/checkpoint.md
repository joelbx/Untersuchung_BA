# Checkpoint

Task: Add ipset set-extension support to the iptables module.
Changes: Added `match_set` and `match_set_flags` documentation, argument validation, automatic `-m set --match-set` rule construction (including inversion), a usage example, unit coverage, and a changelog fragment.
Regression evidence: Temporarily removed the new rule-construction block and ran `python -m pytest test/units/modules/test_iptables.py -q -k 'match_set_rule_with_and_without_explicit_match or match_set_inversion_and_flags'`; both selected tests failed as expected (pytest exit 1). Restored the block afterward.
Verification: `python -m pytest test/units/modules/test_iptables.py -q` passed (25 tests, exit 0). `git diff --check` passed (exit 0).
Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used local fallback search.
