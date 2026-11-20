# Checkpoint

Task: resolve incorrect package lookup when multiple package versions or architectures are installed.

Completed:
- Added shared `base.pkgPs` process enumeration, executable and mapped-file collection, listen-port attachment, and owner-package association.
- Refactored Debian and Red Hat post-scan paths to use `pkgPs` with their distribution-specific ownership lookup.
- Added Red Hat owner-output parsing that ignores permission-denied, unowned-file, and missing-file lines; malformed unexpected lines return errors.
- Matched Red Hat owners to exact scanned package identity when available, with package-name fallback for the existing name-keyed package collection.

Verification:
- `go test ./scan` passed.
- `git diff --check` passed.
