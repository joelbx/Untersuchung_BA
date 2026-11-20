Task: simplify reversetunnel server to one localSite and reuse proxy access point/cache.
Status: implemented single localSite, reused server clients/access point, added validation test, and updated constructor test fixture.
Verification: go test ./lib/reversetunnel -count=1 passed; git diff --check passed.
