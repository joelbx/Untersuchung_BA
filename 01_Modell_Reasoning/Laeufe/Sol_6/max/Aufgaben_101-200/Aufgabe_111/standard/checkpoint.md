# Checkpoint

Task: support Amazon Linux 2023, 2025, 2027, and 2029 detection, advisory lookup, and EOL dates.

Completed:
- Normalized recognized Amazon Linux releases and retained YYYY.MM as Linux 1; unrecognized releases return unknown.
- Added standard support end dates for 2023, 2025, 2027, and 2029 and tests for support boundaries and extended support behavior.
- Parsed newer /etc/system-release forms without the old 2022/2 prefix collision.
- Routed HTTP and local OVAL lookups to the normalized Amazon release, and generated links for ALAS2023 and later listed releases.

Verification: `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./config ./oval ./scanner` passed.
