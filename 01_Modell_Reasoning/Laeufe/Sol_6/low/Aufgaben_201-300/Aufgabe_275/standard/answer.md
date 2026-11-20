Updated `authenticate` to preserve the trace classification of non-access `setupContext` errors while still returning `AccessDenied` for access-related failures. The existing test table now checks the distinction, including the no-tunnel `BadParameter` case.

`go test ./lib/kube/proxy -count=1` passes.