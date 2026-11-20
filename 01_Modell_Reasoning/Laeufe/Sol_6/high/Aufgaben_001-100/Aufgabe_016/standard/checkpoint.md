# Checkpoint

Task: host-scoped monitoring scheduler registration and HAProxy monitor interfaces.
Status: implemented and verified.
Changes: async UTC scheduler with function-name job IDs, hostname allowlist matching, Docker service IP lookup, async monitoring entrypoint, HAProxy CSV to Graphite event pipeline, focused tests.
Verification: `python -m pytest scripts/monitoring/tests -q` (8 passed); Ruff checks passed; import checks on allowed and disallowed hosts produced the expected registered jobs; `git diff --check` passed.
