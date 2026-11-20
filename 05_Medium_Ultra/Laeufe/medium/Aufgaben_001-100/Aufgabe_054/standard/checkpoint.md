Task: Add generic singleton.GetInstance in utils/singleton.
Status: Implemented GetInstance with exact reflect.Type keys and per-type sync.Once. Added value/pointer and 20,000-caller concurrency tests. Verified with GOPROXY=off GOSUMDB=off go test -race ./utils/singleton -count=1 and git diff --check.
