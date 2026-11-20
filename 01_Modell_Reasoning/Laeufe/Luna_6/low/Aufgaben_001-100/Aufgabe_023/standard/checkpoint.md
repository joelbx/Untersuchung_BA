# Checkpoint

Issue: avoid initializing an authentication database when the enabled methods do not need persistent storage.

Plan: locate authentication configuration and startup/cleanup paths; add explicit per-method database requirements; wire requirement checks into initialization and cleanup; run relevant existing tests.
