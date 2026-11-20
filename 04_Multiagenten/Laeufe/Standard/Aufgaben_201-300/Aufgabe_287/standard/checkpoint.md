Task: Track scanned image filenames and persist full album image paths.
Status: Complete. Added album image_files column and model field; migration forces full rescan. Scanner collects image names, carries complete directory map through changed/deleted refreshes, and stores sorted full image paths joined with filepath.ListSeparator. Added focused tests for Dirs, image collection, and path aggregation.
Verification: go test ./model ./scanner ./db ./persistence passed; go test ./model ./scanner passed again after final cleanup; git diff --check passed.
