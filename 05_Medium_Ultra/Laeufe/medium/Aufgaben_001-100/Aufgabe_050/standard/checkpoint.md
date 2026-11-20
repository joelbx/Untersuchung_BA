Task: Fix nullable fields causing scan errors after upgrade; add gg.P and gg.V.
Status: Complete. Album ImageFiles, album/artist ExternalInfoUpdatedAt, and share ExpiresAt/LastVisitedAt are nullable pointers. Read/write call sites use gg.V/gg.P. Added helper and album scan regression tests.
Verification: GOPROXY=off go test ./utils/gg ./persistence ./core ./core/artwork ./scanner ./server/subsonic ./server/public passed; git diff --check passed. Broader test run failed only in unrelated TagLib fixture/permission tests.
