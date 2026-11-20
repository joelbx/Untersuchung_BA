Updated `reversetunnel.Server` to keep one `localSite` and reuse the proxy’s existing access point and clients. Service connections now validate the certificate’s cluster name before registration. Added regression coverage for validation, registration, lookup, proxy updates, and local-site persistence.

Verification: `go test ./lib/reversetunnel -count=1` passed.