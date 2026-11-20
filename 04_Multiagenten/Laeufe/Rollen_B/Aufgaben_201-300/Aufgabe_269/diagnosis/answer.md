I located the data loss in two conversion paths:

- [Convert](/app/contrib/trivy/pkg/converter.go:72) replaces a CVE’s contents with one `trivy` entry on each occurrence. It drops source-specific severity and CVSS data, and a later scan target can erase an earlier one.
- [getCveContents](/app/detector/library.go:227) also creates one `trivy` entry. It omits per-source scores and dates; [DetectLibsCves](/app/detector/library.go:74) does not merge contents when a CVE repeats.
- [CveContent types](/app/models/cvecontents.go:338), [metadata aggregation](/app/models/vulninfos.go:390), and [TUI references](/app/tui/tui.go:948) need to recognize `trivy:<source>` keys for the resulting records to appear.

An [existing parser fixture](/app/contrib/trivy/parser/v2/parser_test.go:350) contains both NVD and Red Hat CVSS data, but expects one unscored `trivy` entry. The fix should preserve each source’s severity, CVSS metrics, references, and dates across repeated CVEs. The exact fields available from the local Trivy DB dependency remain unverified.

**No project source or tests were edited or run.** This run was limited to fault localization; I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).