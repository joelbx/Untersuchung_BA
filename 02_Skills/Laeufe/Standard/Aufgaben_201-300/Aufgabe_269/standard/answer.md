Resolved the Trivy source separation issue. CVE contents now use `trivy:<source>` keys and preserve each source’s severity, CVSS metrics, references, and dates. Repeated findings merge without dropping source data. Model aggregation and TUI references now include the source entries.

The affected Go tests and `git diff --check` pass.