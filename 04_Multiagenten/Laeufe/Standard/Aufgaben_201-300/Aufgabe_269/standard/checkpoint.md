Task: Separate Trivy CVE contents by source across converter, detector, model aggregation, and TUI.
Status: Complete. Added shared source-aware Trivy mapping and merge, source types and aggregation, TUI references, and focused regression tests. Updated parser fixture expectations.
Verification: GOPROXY=off GOTOOLCHAIN=local go test -count=2 ./contrib/trivy/pkg ./contrib/trivy/parser/v2 ./models ./detector ./tui; git diff --check. All passed (TUI has no tests).
Constraints honored: Local code/tests only; no git history, index baseline, or harness configuration changes.
