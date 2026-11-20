# Checkpoint

Task: ingest and expose NVD CVSS v4.0 metrics alongside MITRE entries.
Status: investigating root cause before edits.
Constraints: local evidence only; no downloads, git history/index changes, or harness changes.
Tooling: rg unavailable (`/bin/bash: rg: command not found`); using find/grep.

Root cause evidence: CveContent already has CVSS 4.0 fields. ConvertNvdToModel groups v2/v3 by metric Source, but never iterates Cvss40 or copies its fields into emitted content. Cvss40Scores scans only Mitre. Current go-cve-dictionary version (20240628) lacks Nvd.Cvss40; cached 20240703 version has it, with unchanged dependency go.mod. Hypothesis: using cached dependency version and extending the existing source grouping/copy pattern will make NVD v4 metrics available, while adding Nvd to aggregation order will surface them after Mitre.

Regression results before fixes:
- `GOPROXY=off GOSUMDB=off go test ./models -run '^TestVulnInfo_Cvss40Scores$' -count=1` failed: only MITRE returned, NVD missing.
- After switching to the cached dependency for Nvd.Cvss40, `GOPROXY=off GOSUMDB=off go test -mod=mod ./models -run '^TestConvertNvdToModelCvss40$' -count=1` failed: only the v3-bearing source emitted; v4-only source missing.
Implemented: aggregate Mitre then Nvd; group NVD v4 metrics by Source and copy v4 fields to emitted CveContent. `GOPROXY=off GOSUMDB=off go test -mod=mod ./models -count=1` passed. Downstream reporter/detector tests pending.

Final verification:
- `GOPROXY=off GOSUMDB=off go test -mod=readonly ./models -count=1` passed.
- `git diff --check` passed.
- Attempted `GOPROXY=off GOSUMDB=off go test -mod=readonly ./detector ./reporter/... -count=1`; interrupted after more than 4 minutes of dependency compilation without test output (exit 130). Downstream package result remains unverified; this was a time/resource limit, not a reported test failure.
- No dependencies were downloaded; the newer go-cve-dictionary version was already cached locally.
