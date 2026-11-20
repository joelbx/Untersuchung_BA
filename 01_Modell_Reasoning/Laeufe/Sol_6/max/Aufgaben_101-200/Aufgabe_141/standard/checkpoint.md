# Checkpoint

Task: Add `-wp-ignore-inactive` so WordPress vulnerability scanning can exclude inactive plugins and themes.

Initial state: Working tree clean. Relevant code is in `config`, `commands`, `models`, and `wordpress`; `FillWordPress` lives in `wordpress/wordpress.go`. Next: inspect flag registration and package status handling, implement filtering, then run existing relevant Go tests.

Progress: Added the report and TUI flags, top-level TOML configuration, filtering before WordPress API requests, and a result filter for saved findings. Added focused tests for flag registration, TOML loading, filtered requests/findings, and `removeInactives`.

Final: `GOPROXY=off GOSUMDB=off go test ./config ./wordpress ./models ./commands ./report` passed. The feature is documented in README and the generated config template. No git history or index changes were made.
