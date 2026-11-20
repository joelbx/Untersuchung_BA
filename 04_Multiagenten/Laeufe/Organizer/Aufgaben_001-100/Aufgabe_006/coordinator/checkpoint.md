Task: implement generic concurrent fanoutbuffer in lib/utils/fanoutbuffer.
Status: complete. New package implements configurable ring and overflow, independent cursors, blocking and nonblocking reads, grace expiry, cleanup, and close semantics. No delegation used.
Verification: go test -race ./lib/utils/fanoutbuffer passed; go test ./lib/services -run Fanout -count=1 passed.
