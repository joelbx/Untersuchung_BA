# Checkpoint

Issue: unreliable persisted session retrieval on public pages.
Status: implementation complete.
Changes: unified persisted-session selection, public provider auth state, public user localID, SRP headers, telemetry, mirrored drive-store paths, parse-error reporting.
Verification: focused Drive and drive-store tests pass (13 each); Prettier and diff checks pass; TypeScript is blocked only by an existing packages/crypto OpenPGP type mismatch.
