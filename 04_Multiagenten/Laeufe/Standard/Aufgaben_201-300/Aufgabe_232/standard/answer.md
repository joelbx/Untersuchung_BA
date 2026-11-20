Implemented OS EOL lookup and scan warnings. The canonical dates and family identifiers are in [config/os.go](/app/config/os.go); scans add lifecycle warnings to each target’s results, and the summary prints them in order with the required `Warning: ` prefix. Major version parsing is available through `util.Major`.

`go test ./config ./util ./scan ./report` and `git diff --check` passed.