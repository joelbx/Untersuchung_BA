# Checkpoint

Task: make `getOpenSubsonicExtensions` public while retaining JSON formatting and exactly three advertised extensions.

Status: investigation started. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find` instead. No repository changes yet.

Root cause: `api.routes` installs `checkRequiredParameters` and `authenticate` on the root Chi mux before registering `getOpenSubsonicExtensions`. The handler already returns exactly `transcodeOffset`, `formPost`, and `songLyrics`; `sendResponse` uses `req.Params` to honor `f=json`. Chi's `With` scopes middleware to registered routes while sharing the route tree. A regression test for the public `.view?f=json` route has been added and its pre-fix run is in progress.

Resolution: registered `getOpenSubsonicExtensions` on the root router after `postFormToQueryParams`, and enclosed all other routes in a Chi group with `checkRequiredParameters`, `authenticate`, and last-access middleware. The handler and shared JSON formatter were unchanged.

Verification:
- Before fix: `go test ./server/subsonic -run TestSubsonicApi -ginkgo.focus='getOpenSubsonicExtensions route' -count=1` failed as expected: response status `failed` instead of `ok`.
- After fix: `go test ./server/subsonic -run TestSubsonicApi -ginkgo.focus='getOpenSubsonicExtensions route' -count=1` passed.
- After final test additions: `go test ./server/subsonic ./server/subsonic/responses -count=1` passed both packages.
- `git diff --check` passed.
