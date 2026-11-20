# Checkpoint

Task: fix process-to-package lookup for overlapping RPM package versions and architectures.
Status: completed. Shared pkgPs associates processes using file ownership; Debian and Red Hat postScan use it. Red Hat needs-restarting also uses ownership names. RPM ownership parsing skips the three specified file errors, rejects malformed lines, and deduplicates owners.
Verification: go test ./scan -count=1 passed; git diff --check passed.
Constraints: local repository only; git history, index baseline, and harness configuration untouched.
