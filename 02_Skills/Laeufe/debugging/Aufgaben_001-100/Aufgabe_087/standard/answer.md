Added opt-out telemetry with a persistent per-host UUID, four-hour `flipt.ping` reporting, version metadata, and nonfatal error logging. The advanced config example disables telemetry. I also added the `internal/info.Flipt` HTTP handler.

`GOPROXY=off go test ./... -count=1` and `git diff --check` passed.

**Delivery limit:** the issue specifies no collection endpoint. The reporter targets `https://telemetry.flipt.io/v1/track`; local tests verify the request and error handling, but live delivery was not verified.