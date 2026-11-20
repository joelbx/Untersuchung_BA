# Voice broadcast liveness

Status: implemented the liveness union, grey badge style, typed header call sites, playback liveness events, hook subscription, final-chunk detection, and grey paused recording badges. Updated three playback body snapshots and one recording PIP snapshot. All 24 voice broadcast suites passed (225 tests) before the final recording badge change; its two focused suites passed afterward (10 tests). The final model and chunk utility tests passed again (64 tests). ESLint, stylelint, and `git diff --check` passed. `rg` is unavailable, so searches used `find` and `grep`.

The full TypeScript check was repeated after the final edit and remains blocked by a pre-existing error in unchanged `src/utils/notifications.ts:79` (TS2554, 3 arguments supplied where 1–2 are accepted). No issue-related type errors were reported.
