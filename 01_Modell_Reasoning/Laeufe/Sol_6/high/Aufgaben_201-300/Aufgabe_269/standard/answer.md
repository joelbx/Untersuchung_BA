Trivy CVE data is now stored under `trivy:<source>` keys, with each source’s severity, CVSS values, references, and publication dates preserved. I updated the model aggregators and TUI to include those entries, and revised the parser fixtures and focused tests.

The affected package tests passed with network access disabled, and `git diff --check` passed.