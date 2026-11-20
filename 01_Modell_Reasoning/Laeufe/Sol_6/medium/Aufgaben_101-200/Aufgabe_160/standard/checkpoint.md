Task: fix Direct Dial wildcard node addresses using inventory stream peer address.
Implemented: upstream stream PeerAddr, pipe option, gRPC peer capture, SSH heartbeat host rewrite preserving port, regression tests.
Verification: targeted api/client and lib/inventory tests passed using root module with GOPROXY=off; git diff --check passed.
