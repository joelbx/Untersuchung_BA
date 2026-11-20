Task: refactor detectScanDest to grouped, deduplicated, ordered ports by IP.
Status: complete. Updated scanner consumer and regression tests. go test ./scan -count=1 and git diff --check passed.
