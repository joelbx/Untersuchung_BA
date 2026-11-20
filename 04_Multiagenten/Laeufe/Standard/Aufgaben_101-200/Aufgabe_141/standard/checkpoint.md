# Checkpoint

Task: add `-wp-ignore-inactive` and skip inactive WordPress plugins/themes.

Implemented: scan and report flags; global config/TOML field; filtering before WordPress API requests; existing per-server option shares that early filter; result-level CVE filtering recognizes global and scan-saved settings. Added tests for TOML loading and package filtering.

Verification: `GOPROXY=off GOSUMDB=off go test ./wordpress ./config ./commands ./models` passed. `git diff --check` passed. No external research or downloads.
