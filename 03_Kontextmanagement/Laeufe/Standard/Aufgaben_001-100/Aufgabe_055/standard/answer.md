Updated the Trivy parser to store the OS name as `Release`, use `ArtifactName` as `ServerName` for OS and library scans, append `:latest` to untagged container image names, and leave `Optional` nil.

Package CVE detection now skips OVAL and GOST when the required metadata is missing or the scan type is unsupported. Trivy results are identified through `ScannedBy`, preserving their existing CVEs. Detection errors are logged and returned.

The relevant parser and detector tests pass, and `git diff --check` is clean.