Task: Align OS EOL datasets and Windows KB mappings.
Status: complete.
Changes: updated Fedora 37/38 dates and added 40; added SUSE Enterprise Desktop/Server 13/14 dates; marked macOS 11 ended and added 15; extended Windows 10 19045, Windows 11 22621/22631, and Server 2022 20348 rollups using named literals in revision order; updated and added existing-package tests.
Validation: go test ./config ./scanner passed; GOPROXY=off targeted config/scanner tests passed; git diff --check passed.
