# Checkpoint

Located the centralized playback method in `src/LegacyCallHandler.tsx`. The call sound identifiers were module-private, and playback called `play()` without correcting `muted`. Exported the identifier enum and set `muted = false` immediately before playback (idempotent for already-unmuted elements). Next: inspect test coverage and run existing relevant tests.
