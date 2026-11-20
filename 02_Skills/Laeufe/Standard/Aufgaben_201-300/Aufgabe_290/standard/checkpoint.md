Task: fix muted call sound playback.
Changes: export AudioID identifiers; unmute the selected media element immediately before every play attempt; add public handleEvent media listener and register its debug setting; add playback tests for all four sounds and already unmuted audio.
Checks executed:
- ./node_modules/.bin/jest test/LegacyCallHandler-test.ts --runInBand --silent: passed (14 tests).
- ./node_modules/.bin/tsc --noEmit --jsx react: passed.
- ./node_modules/.bin/eslint src/LegacyCallHandler.tsx src/legacy/LegacyCallHandler/handleEvent.ts src/settings/Settings.tsx test/LegacyCallHandler-test.ts: passed.
- git diff --check: passed.
Note: rg was unavailable (/bin/bash: rg: command not found); used find and grep for local inspection. No downloads attempted.
