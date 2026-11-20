# Checkpoint

Issue: prevent `tsh device enroll --current-device` from panicking when registration succeeds but enrollment is rejected at the device limit.

Plan: inspect the local enrollment ceremony, fake device service, test environment, and existing tests; implement the requested behavior; run relevant existing tests.
