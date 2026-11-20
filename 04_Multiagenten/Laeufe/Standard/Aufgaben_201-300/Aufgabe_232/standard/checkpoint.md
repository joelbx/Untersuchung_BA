Task: implement canonical OS EOL lookup, scan warnings and summary rendering, and centralized major version parsing.
Status: complete. Canonical dates and family constants are in config/os.go; scan/eol.go evaluates warnings with a supplied time; scan/base.go attaches them to results; report/util.go renders each warning in order with `Warning: `; util.Major exposes centralized parsing.
Verification: go test ./config ./util ./scan ./report passed; git diff --check passed. SQLite C compiler emitted an existing warning during build but tests succeeded.
Constraints observed: local repository and tests only; git history, index baseline and harness configuration untouched.
