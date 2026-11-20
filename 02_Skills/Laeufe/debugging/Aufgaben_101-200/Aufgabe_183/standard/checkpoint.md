# Checkpoint

Task: Correct Ubuntu 20.04 extended support and add Ubuntu 22.04 lifecycle metadata.
Status: Investigating repository behavior and tests before editing lifecycle data.
Checks: Pending.

Investigation: `config.GetEOL` maps Ubuntu releases by exact version. Its 20.04 entry lacks `ExtendedSupportUntil`; `IsExtendedSuppportEnded` then falls back to the standard date. The 22.04 key is absent, so `CheckEOL` reports unknown release. Existing 18.04 entry demonstrates both date fields, and `ScanResult.CheckEOL` consumes the same lookup.
Hypothesis: Adding the two specified metadata entries will correct support transitions and release recognition without changing detection or warning logic.

Regression: Added `TestUbuntuLTSSupportDates`. Before the map edit, `GOTOOLCHAIN=local GOPROXY=off go test ./config -run '^TestUbuntuLTSSupportDates$' -count=1` failed as expected: 20.04 extended date was zero and 22.04 was not found.
Fix: Added 20.04 extended support through 2030-04-01 23:59:59 UTC; added 22.04 standard and extended support through 2027-04-01 and 2032-04-01 23:59:59 UTC. Existing date convention is end-of-day UTC.
Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./config -count=1` passed; `GOTOOLCHAIN=local GOPROXY=off go test ./models ./scanner -count=1` passed; `git diff --check` passed.
