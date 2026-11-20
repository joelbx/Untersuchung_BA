# Checkpoint

Task: Align OS EOL data and Windows KB mappings, preserve existing data, verify compilation and detection.

Status: Investigating repository state and reproducing the issue before edits.

Constraints: Local sources only; no downloads, credentials, private process files, benchmark artifacts, git history/index/harness changes.

## Investigation

`GetEOL` uses hard-coded map entries and `IsStandardSupportEnded` compares the UTC timestamp directly. Fedora 37/38 have older dates; 40 is missing; macOS 11 is an empty record and 15 is missing; SUSE Desktop/Server 13/14 are absent. The three Windows rollup slices end at October 2023 revisions. `DetectKBsFromKernelVersion` walks each slice in revision order, placing later KBs in Unapplied and earlier KBs in Applied. Existing Windows tests assert complete slices, so extending data requires updating those expectations. No pre-existing working-tree changes. New rollup records should follow the existing named literal pattern.

Hypothesis: updating those hard-coded records and appending ordered rollups is sufficient; detection logic should remain unchanged. Tests will first reproduce missing EOL data and KB classification.

## Implementation and checks

A pre-fix local reproduction failed with `AssertionError: Fedora 40 missing` for the absent map entry. Added Go regression tests for EOL timestamps, ordered KB maps, and old/high kernel revision classification. Updated only requested EOL map records and appended named rollup literals in revision order. Existing scanner test expectations were extended to cover the new KBs. `go test -p 2 ./config ./scanner -count=1` initially failed because older Fedora expectations in `config/os_test.go` still asserted the prior dates and missing Fedora 40; those expectations were updated. The same command then passed: config and scanner both `ok`. `git diff --check` passed. Repository-wide compile check is running.

Final verification: `go test -p 2 ./config ./scanner -count=1` passed for both packages. `go test -p 2 ./... -run '^$' -count=1` passed for all packages (compilation check). `git diff --check` passed. No offline tooling failures remain. Added tests cover Fedora/SUSE/macOS EOL records, ordered rollups, shared Windows 11 build mappings, and kernel revision classification.
