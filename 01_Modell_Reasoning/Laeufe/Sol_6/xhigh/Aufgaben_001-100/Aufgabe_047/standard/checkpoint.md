# Checkpoint

Task: Implement deterministic per-identifier seeding and reseeding in utils/hasher/hasher.go.
Status: Complete.
Changes: Exported Hasher; added package and method SetSeed; stored caller-provided string seeds per ID; reused one process-wide maphash seed; initialized missing ID seeds automatically; synchronized seed access; added restore, cross-instance, and global API tests.
Verification: go test ./utils/hasher; go test -race ./utils/hasher; go test ./db ./persistence; git diff --check. All passed with GOPROXY=off and GOSUMDB=off.
Constraint: Git history, index baseline, and harness configuration unchanged.
