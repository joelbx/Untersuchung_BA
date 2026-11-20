Implemented peer-address propagation for inventory control streams and used it to replace wildcard or local SSH heartbeat hosts while preserving the heartbeat port.

`go test ./lib/inventory` passed. The API client tests could not run: `GOPROXY=off` and `github.com/gogo/protobuf@v1.3.2` is unavailable locally.

Changes are in [inventory.go](/app/api/client/inventory.go) and [controller.go](/app/lib/inventory/controller.go).