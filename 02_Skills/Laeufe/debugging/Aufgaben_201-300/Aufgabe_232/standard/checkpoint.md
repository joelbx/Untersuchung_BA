# Checkpoint

Task: add canonical OS EOL lookup, per-target scan warnings, summary rendering, and shared major-version parsing.

## Investigation

- `scan.GetScanResults` copied each target's scan model into results without any EOL evaluation.
- `report.formatScanSummary` rendered a warnings slice as one Go value, so individual warning text and order were not represented with the required prefix.
- EOL mappings did not exist. Major extraction was duplicated in `config`, `oval`, and `gost`; the `oval` parser assumed a dot and could panic for dotless versions.
- OS detection yields patch releases (`7.9`, `11.4-RELEASE`, `18.04.6`) while requested lifecycle keys use major or major.minor versions. Amazon uses its own release keys.
- Failing reproductions were run before fixes: `GOPROXY=off go test ./config -run TestEOLLookupAndBoundaries -count=1` failed on undefined `GetEOL`; `GOPROXY=off go test ./scan -run TestAppendEOLWarningsNormalizesDetectedRelease -count=1` returned missing-mapping warnings for detected patch releases; `GOPROXY=off go test ./config -run TestAmazonMajorVersionSingleTokenTwo -count=1` reported major version 1 for Amazon release `2`.

## Implementation

- Added exact family/release lifecycle table and EOL evaluators in `config/os.go`, with OS family constants in the same file. `Ended` marks entries whose standard and extended end dates are the same; phase checks use strict `now.After` and treat absent extended dates as not applicable.
- Added per-target EOL warning evaluation in `scan`, using the supplied scan timestamp and normalizing detected patch releases only at the scan lookup boundary. `GetEOL` itself remains exact-key lookup.
- Summary prints each warning separately in evaluation order with `Warning: `.
- Shared major parser lives in `version`, with public `util.Major`; existing package callers delegate to it. The small `version` package avoids a `config`/`util` import cycle.

## Verification

- `GOPROXY=off go test ./config ./util ./scan ./report ./oval ./gost -count=1` passed before the final boundary test was added.
- A repeat of that command with the final boundary test passed (exit code 0).
- `git diff --check` passed.
