Implemented HA database service selection and display deduplication.

The proxy now keeps all matching servers, shuffles them through the configurable hook, and tries each candidate when dialing reports a connection problem. If every candidate fails, it returns an error stating that no candidate database service could be reached. I also added `HostID` to server strings, sorted servers by name then host ID, added the deduplication helper, and added fake per-server tunnel outages.

Validation passed: `go test ./types` in `/app/api`, and `go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh` in `/app`. `git diff --check` passed.