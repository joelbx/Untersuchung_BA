Updated Trivy conversion to keep separate `trivy:<source>` CVE contents, including each source’s severity, CVSS values, references, and dates. Repeated CVEs now retain content from multiple scan targets. Metadata aggregation and TUI references include the source-specific entries.

Verification: `git diff --check` and tests for the converter, detector, models, and TUI packages passed.