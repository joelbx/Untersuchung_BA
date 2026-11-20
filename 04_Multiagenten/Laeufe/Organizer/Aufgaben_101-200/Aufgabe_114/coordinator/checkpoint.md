# Checkpoint

Task: prefer artist.* in artist folder, persist album media directories, and trace lookup durations.
Status: implemented and verified.
Changes: album media_file_dirs migration and model accessor; scanner's ToAlbum now populates directories; artist reader derives common album parent and checks artist.* first; artwork source attempts log duration; focused tests added.
Tests: go test ./model ./core/artwork ./scanner ./db ./persistence (passed); git diff --check (passed).
Delegation: none.
