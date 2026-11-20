# Checkpoint

Task: consolidate reversetunnel.Server to one localSite and reuse the proxy resource cache.
Status: complete.
Changes: server owns one localSite; local site uses server LocalAccessPoint, localAuthClient, and PeerClient; service connections validate the certificate cluster against the local domain; site operations use the one instance. Added validation and cache reuse assertions.
Verification: go test ./lib/reversetunnel -count=1 passed; git diff --check passed.
