Verified nullable schema fields and updated models plus call sites. Added gg.P/gg.V and tests for zero/nil behavior and NULL scans for album, artist, and share.
Validation: GOPROXY=off go test ./utils/gg ./model ./persistence ./scanner ./core/... ./server/subsonic ./server/public passed; persistence rerun passed; git diff --check clean.
