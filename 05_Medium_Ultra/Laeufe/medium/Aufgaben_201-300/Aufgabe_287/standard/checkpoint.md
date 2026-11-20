Task: Add album image paths gathered during scans, with migration and rescan.
Status: Implemented and verified. The scanner gathers image names, waits for the complete directory map, and writes full paths to albums. Migration adds image_files and forces a full rescan.
Tests: go test ./scanner ./model ./persistence passed; git diff --check passed.
Constraints: Local code/tests only; git history and index baseline unchanged.
