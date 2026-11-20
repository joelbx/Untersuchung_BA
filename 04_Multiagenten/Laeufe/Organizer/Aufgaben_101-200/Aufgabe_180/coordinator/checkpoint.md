# Checkpoint

Task: align OS EOL data and Windows rollup KB mappings.
Status: implemented and verified.
Changes: Fedora 37/38 cutoffs and Fedora 40; SUSE Enterprise Desktop/Server 13/14; macOS 11 ended and 15 present; Windows 10 19045, Windows 11 22621/22631, Server 2022 20348 rollups extended using named struct literals; regression tests updated and added.
Verification: go test ./config ./scanner (passed); go build ./... (passed); git diff --check (passed).
Delegation: none; solved directly.
