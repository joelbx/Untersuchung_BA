# Checkpoint

Task: Correct Red Hat RPM installed package, repoquery, source filename, and update candidate parsing.

Status: Implementation complete and verified.

Changes:
- Preserve empty release columns in installed RPM and repoquery output.
- Build binary and source versions consistently across epoch and release combinations.
- Parse source filenames ending in either `.src.rpm` or `-src.rpm`, including empty release, and reject malformed components.
- Preserve empty release and normalize `(none)` epoch in update candidate listings.
- Add regression coverage for installed packages, source filenames, and CentOS/Amazon updates.

Verification: `GOPROXY=off GOSUMDB=off go test ./scanner -count=1` passed. `git diff --check` passed.
