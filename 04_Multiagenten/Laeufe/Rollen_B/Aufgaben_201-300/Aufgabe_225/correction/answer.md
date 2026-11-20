Updated the report summaries, vulnerability details, and TUI to display KEVs from the dedicated `KEVs` field. Older JSON with CISA alerts remains supported. Added regression tests for the summary and report output.

The reviewer’s exact command, `GOPROXY=off GOSUMDB=off go test ./models ./detector`, passed. The broader `./models ./detector ./reporter ./tui` run also passed; TUI has no test files.