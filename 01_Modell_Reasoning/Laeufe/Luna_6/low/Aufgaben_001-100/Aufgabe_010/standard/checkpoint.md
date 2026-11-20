# Checkpoint

Implemented the composer and reply preview updates:
- Tombstone notice uses a paragraph element and preserves the existing localized status message and replacement link.
- Added reusable `CancelButton` in `src/components/views/buttons/Cancel.tsx` with a configurable pixel size, AccessibleButton behavior, consistent CSS sizing, and an accessible default label.
- Reply preview uses the shared cancel control, labels it “Cancel reply”, and identifies the reply target by display name or Matrix user ID.
- Reply preview cancel dimensions now use the shared CSS custom property.

Verification completed:
- `npm test -- --runInBand test/components/views/rooms/MessageComposer-test.tsx` passed.
- `npx tsc --noEmit --jsx react` passed.

Profile rendering uses the existing shared `DisambiguatedProfile` through `SenderProfile`, with a default RoomContext; no profile behavior change was needed for these requirements.
