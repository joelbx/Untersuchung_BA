VERDICT: ACCEPT

The patch registers `getOpenSubsonicExtensions` outside authentication. The existing route tests verify unauthenticated `?f=json` responses on both URL forms and the exact three extensions: `transcodeOffset`, `formPost`, and `songLyrics`.

`GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./server/subsonic -run TestSubsonicApi -count=1` passed. `git diff --check` passed. No code defect or TEST_ENVIRONMENT_PROBLEM found.