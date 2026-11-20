Fixed the Kubernetes proxy’s `authenticate` path to preserve non-access `setupContext` errors while returning `AccessDenied` for access-related failures. Updated the classification checks in [forwarder_test.go](/app/lib/kube/proxy/forwarder_test.go).

`TestAuthenticate` and the full `lib/kube/proxy` test suite pass.