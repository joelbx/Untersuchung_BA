Updated `reversetunnel.Server` to keep one `localSite` and have that site reuse the proxy’s existing access point. Service connections now validate the certificate’s cluster name before registering with that site. Added tests for validation, connection registration, and access point reuse.

`go test ./lib/reversetunnel -count=1` and `git diff --check` passed.