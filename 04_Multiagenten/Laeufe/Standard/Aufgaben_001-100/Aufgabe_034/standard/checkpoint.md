Task: normalize Internet Archive publisher/place and ISBN metadata in Open Library editions.
Status: implemented public normalization helpers in upstream/utils.py and wired them into get_ia_record. Updated and added focused tests. Both affected test files pass (26 tests); git diff --check passes.
