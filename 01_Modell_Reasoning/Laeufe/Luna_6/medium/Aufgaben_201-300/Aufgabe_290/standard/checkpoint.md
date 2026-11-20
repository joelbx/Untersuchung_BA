Issue: call audio requests must unmute their media elements before playback, with stable exported call sound identifiers.

Implemented in src/LegacyCallHandler.tsx: exported AudioID enum (ring, ringback, call end, busy) and set audio.muted = false immediately before audio.play(). The assignment is idempotent for already-unmuted elements.

Verification: `yarn test --runInBand test/LegacyCallHandler-test.ts` passed (9 tests); `yarn eslint src/LegacyCallHandler.tsx` passed.

Repository note: the interface references src/legacy/LegacyCallHandler/handleEvent.ts, which does not exist in this checkout. No handleEvent API was added because the issue concerns call sound playback and there is no corresponding event listener module in the snapshot.
