# Checkpoint

Implemented first-class KEV support in `VulnInfo.KEVs` with CISA and VulnCheck model types, source-specific metadata, feed conversion, invalid due-date normalization, KEV summary reporting, and JSON sorting by source then vulnerability name. `AlertDict.CISA` remains for legacy JSON compatibility; new KEV detections populate `KEVs` directly.

Validation passed: `GOPROXY=off GOSUMDB=off go test ./models ./detector ./reporter`; `git diff --check` passed. `rg` is unavailable, so repository searches used `find` and BusyBox `grep`.
