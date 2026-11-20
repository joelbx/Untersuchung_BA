# Checkpoint

Issue: preserve trace error classifications from Kubernetes proxy authentication setup.

Investigation: `Forwarder.authenticate` wraps every `setupContext` error as `AccessDenied`. `setupContext` already emits access errors for authorization failures such as remote user access, and emits `BadParameter` when remote routing has no reverse tunnel. The fix should return existing access errors unchanged (or as wrapped) while preserving other setup errors. Existing proxy tests are in `lib/kube/proxy/forwarder_test.go`.

Next: inspect test table coverage and add assertions for setup failures, then run the focused package tests.
