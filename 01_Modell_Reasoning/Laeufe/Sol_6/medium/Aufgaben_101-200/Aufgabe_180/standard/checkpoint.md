Task: align OS EOL datasets and Windows KB mappings.
Status: complete. Updated config/os.go and scanner/windows.go, updated existing expectations and added focused tests.
Verification: go test ./config ./scanner passed; git diff --check passed.
Constraints observed: local repository/tests only; git history and index untouched.
