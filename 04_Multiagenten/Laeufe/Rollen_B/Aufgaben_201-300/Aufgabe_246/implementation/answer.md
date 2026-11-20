Vulnerability reports now carry the lockfile path and use `(path, library name)` to resolve the installed version. Scanning processes lockfiles separately, and findings that share a CVE retain entries from each file, including findings without a fixed version.

The pinned fanal release has no `AnalyzeFile` API, so the scan uses its available `GetLibraries` API with one in-memory file per call.

Tests pass for `models`, `scan`, `report`, `libmanager`, and the Trivy parser; `git diff --check` also passes.