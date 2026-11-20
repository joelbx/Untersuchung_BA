Implemented multi-device U2F authentication. The server now issues challenges for every registered U2F token while retaining the legacy single-challenge fields; the CLI accepts either format, and the web authentication API carries the enhanced payload.

A focused two-device compatibility test and `go test ./lib/auth ./lib/client ./lib/web ./tool/tsh` passed. This work item is complete.