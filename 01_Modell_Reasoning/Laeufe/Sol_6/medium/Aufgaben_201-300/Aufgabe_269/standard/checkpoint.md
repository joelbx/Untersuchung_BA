Task: Separate Trivy CVE contents by source and preserve source-specific severity, CVSS, references, and dates.
Status: Completed repository edits. Shared Trivy conversion now creates trivy:<source> contents from VendorSeverity/CVSS, with fallback for older results. Library detection uses the same conversion and merges source contents. Model aggregation and TUI include Trivy sources. Added converter regression coverage.
Verification: go test ./contrib/trivy/pkg ./models ./detector ./tui passed; git diff --check passed.
