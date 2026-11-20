Task: separate Trivy CVE contents by source.
Status: implemented and verified.
Changes: source-specific contents in converter and library detector; source severity/CVSS, references and dates preserved; repeated CVEs retain distinct entries. Models aggregate source metadata; TUI includes source references. Parser fixture comparison updated for the new content shape; focused regression tests added.
Validation: go test ./contrib/trivy/pkg ./contrib/trivy/parser/v2 ./models ./detector ./tui; git diff --check. Both passed.
Constraints: local code/tests only; git history, index baseline, and harness configuration untouched.
