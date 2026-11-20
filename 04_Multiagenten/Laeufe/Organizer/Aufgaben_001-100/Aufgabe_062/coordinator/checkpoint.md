Task completed: terminal restoration after canceled/closed password reads and tsh exit.
Implemented ContextReader.maybeRestoreTerm, cancellation/Close restoration, NotifyExit for stdin singleton, and tsh main exit hooks. Added regression tests for cancellation, deadline, clean read recovery, Close, restore error, and NotifyExit.
Validation: GOPROXY=off GOSUMDB=off go test ./lib/utils/prompt passed; GOPROXY=off GOSUMDB=off go test ./tool/tsh -run '^$' passed; git diff --check passed.
Delegation: none.
