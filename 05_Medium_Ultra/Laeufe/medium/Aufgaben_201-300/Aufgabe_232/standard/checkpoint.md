Task: implement canonical OS EOL lookup, scan warnings, and centralized major version parsing.
Status: complete. Canonical dates and evaluators added in config/os.go; scan results append ordered EOL warnings; summary prints each with Warning: prefix; major parsing shared across config, util, OVAL, and GOST. Focused tests added.
Verification: go test ./config ./util ./scan ./report ./oval ./gost passed. git diff --check passed.
Constraints honored: local code/tests only; no git history, index baseline, or harness configuration changes.
