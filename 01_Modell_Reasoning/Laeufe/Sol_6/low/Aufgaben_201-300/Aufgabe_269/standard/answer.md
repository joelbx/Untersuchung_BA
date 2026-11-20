Updated both Trivy conversion paths to keep separate `trivy:<source>` CVE contents, including each source’s severity, CVSS values, references, and publication dates. Model aggregation and TUI references now include those entries.

Added a regression test for one CVE reported by Debian and Ubuntu with different scores. The relevant Go package tests and `git diff --check` pass.