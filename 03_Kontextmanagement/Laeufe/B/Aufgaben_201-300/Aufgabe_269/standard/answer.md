Completed the Trivy source separation fix in `/app`. CVE contents now retain each source’s severity, CVSS values, references, and dates, including when the same CVE appears in multiple targets. The metadata views and TUI now include the source entries.

The relevant Go tests pass, and `git diff --check` is clean.