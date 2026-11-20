Updated `reversetunnel.Server` to keep one `localSite` and reuse the proxy’s existing access point and clients. Local service connections now validate the certificate’s cluster name before registering on that site. Added regression coverage for validation, registration, lookup, and tunnel close.

`go test ./lib/reversetunnel -count=1` and `git diff --check` passed.