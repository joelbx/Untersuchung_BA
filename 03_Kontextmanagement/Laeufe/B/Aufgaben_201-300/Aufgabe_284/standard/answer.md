Resolved the reverse tunnel issue. `Server` now keeps one `localSite`, and that site reuses the proxy’s existing access point and clients. Local service connections validate the certificate’s cluster name before registration.

Added focused tests; `go test ./lib/reversetunnel -count=1` passes.