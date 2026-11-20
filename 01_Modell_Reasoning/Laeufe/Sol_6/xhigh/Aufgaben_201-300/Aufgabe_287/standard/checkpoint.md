Task: Track scanned image file paths on albums.
Status: Complete. Added album image_files field and migration with forced full rescan. Scanner collects image names and refreshes albums using the complete directory map; MediaFiles.Dirs returns sorted unique directories. Added scan, aggregation, refresh, and persistence coverage.
Verification: GOPROXY=off GOSUMDB=off go test ./model ./scanner ./persistence ./db/... passed; git diff --check passed.
