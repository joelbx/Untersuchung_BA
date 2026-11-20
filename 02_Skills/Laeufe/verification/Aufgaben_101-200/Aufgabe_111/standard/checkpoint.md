# Checkpoint

Task: Support Amazon Linux 2023, 2025, 2027, and 2029 detection, advisory lookup, and EOL mappings.

Implemented:
- Normalize recognized Amazon releases and YYYY.MM legacy releases; reject unknown releases.
- Add EOL dates for 2023 (2029-06-30), 2025 (2030-06-30), 2027 (2032-06-30), and 2029 (2034-06-30), all at 23:59:59 UTC.
- Parse newer `/etc/system-release` formats and pass the normalized release to both OVAL lookup paths; add ALAS2023 advisory links.
- Add tests for normalization, EOL dates and support phase boundaries, and OVAL release selection.

Verification: `GOPROXY=off GOSUMDB=off go test -count=1 ./config ./scanner ./oval && git diff --check` exited 0; all three packages passed and the diff check was clean.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`), so local grep/find were used. No downloads were requested.

Uncertainty: External research is prohibited, so future Amazon Linux lifecycle dates could not be independently checked against an AWS source. The mappings use the requested release schedule and the locally established June 30 end-of-day convention.
