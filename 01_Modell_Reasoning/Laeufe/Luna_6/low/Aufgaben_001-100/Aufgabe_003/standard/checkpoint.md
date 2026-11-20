# Checkpoint

Issue: propagate integer `timeOffset` through FFmpeg transcoding and media streaming, parse it at public endpoints, and expose OpenSubsonic support.

Work plan:
1. Inspect repository guidance, current function signatures, command templates, and existing tests/mocks.
2. Update FFmpeg command generation and stream call chains/cache keys/endpoints.
3. Update matching tests and run relevant existing test suites.
