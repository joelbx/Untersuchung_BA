Task: Fix RPM package, repoquery, source RPM filename, and update candidate parsing in scanner/redhatbase.go.
Status: complete. Updated parser and regression tests in scanner/redhatbase_test.go.
Decisions: preserve empty query fields while accepting tab separators; keep binary Package.Version separate from Release per models.Package; source package Version includes release only when present; accept -src.rpm as source architecture form and validate filename components.
Verification: GOPROXY=off go test ./scanner -count=1 passed; git diff --check passed.
Constraints observed: local repository only; no git history, index baseline, or harness configuration changes.
