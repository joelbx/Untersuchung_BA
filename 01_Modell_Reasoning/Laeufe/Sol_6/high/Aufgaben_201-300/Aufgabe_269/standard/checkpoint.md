Task: separate Trivy CVE contents by source in converter and library, update model aggregation and TUI, preserve scoring/severity/dates/references.
Status: complete. Converter and library now create trivy:<source> contents from VendorSeverity and CVSS, preserving CVSS fields, references, and dates. Repeated CVEs retain entries from different sources. Model source constants and aggregation include Trivy sources; TUI displays their references. Parser fixtures and focused tests updated.
Verification: GOPROXY=off GOSUMDB=off go test ./contrib/trivy/pkg ./contrib/trivy/parser/v2 ./models ./detector ./tui (passed); git diff --check (passed).
Constraints observed: local code/tests only; git history, index baseline, and harness configuration untouched.
