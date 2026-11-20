# Checkpoint

Task: distinguish newly detected and resolved CVEs in scan diff reports.
Status: implemented and verified.
Changes: added DiffStatus, CveIDDiffFormat, CountDiff; diff accepts plus/minus booleans and selects CVEs by presence; package details come from the corresponding scan; added report and TUI flags with both enabled by default; rendered statuses in text, CSV, TUI, Slack, and Telegram; documented flags.
Verification: GOPROXY=off GOSUMDB=off go test ./models ./report ./subcmds passed. git diff --check passed.
Constraints followed: local repository only; no git history, index baseline, or harness configuration changes.
