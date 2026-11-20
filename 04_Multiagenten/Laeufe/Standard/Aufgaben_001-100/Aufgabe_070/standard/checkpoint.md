# Checkpoint

Task: normalize alternative language identifiers and deduplicate format_languages output.
Status: complete.
Changed: catalog language formatting now accepts ISO-639-1 codes, English/native names, and deduplicates by canonical key; tests cover reported cases and an ISO code absent from the direct map.
Verified: 132 catalog utility and add-book tests pass; ruff and git diff --check pass.
