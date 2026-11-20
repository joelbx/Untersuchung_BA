# Checkpoint

Task: Ensure call sound playback unmutes media elements before playing and expose stable public sound identifiers.

Status: Complete. Exported AudioID for ring, ringback, busy, and call-end; unmuted each sound immediately before playback, including queued replay; added the public handleEvent listener and registered its debug setting.

Validation: 18 focused Jest tests passed; TypeScript check passed; ESLint on changed source and tests passed; git diff --check passed.
