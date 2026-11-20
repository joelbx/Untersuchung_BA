# Checkpoint

Task: align OS EOL data and Windows KB mappings, then run relevant existing tests.
Status: complete.
Changes: Fedora 37/38/40, macOS 11/15, FreeBSD 13/14 dates, 51 named Windows KB entries across 19045/22621/22631/20348, and updated tests for EOL and KB classification boundaries.
Validation: gofmt and git diff --check passed; GOPROXY=off GOSUMDB=off go test ./config -count=1 passed; GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_windows_detectKBsFromKernelVersion|TestDetectKBsFromKernelVersionRecentRollups' -count=1 passed. Checked each changed Windows list against HEAD: all prior entries preserved, new revisions ordered and unique.
Interpretation: issue calls the 13/14 dates SUSE Enterprise, but repository and vendor version sequence place them under FreeBSD; SUSE has 11/12/15 releases. Existing SUSE entries remain intact.
