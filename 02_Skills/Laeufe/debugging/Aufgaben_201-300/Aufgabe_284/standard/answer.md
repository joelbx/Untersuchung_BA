Updated `reversetunnel.Server` to keep one `localSite` and use it for connection registration, site lookup, reconnect notices, and proxy fan-out. The local site now reuses the proxy’s existing access point instead of creating another resource cache. Service connections also reject empty or mismatched certificate cluster names.

The reverse tunnel package tests and `git diff --check` pass.