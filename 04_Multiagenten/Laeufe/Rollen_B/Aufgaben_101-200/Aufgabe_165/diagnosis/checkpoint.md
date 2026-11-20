Fault localization complete. No project source or tests edited.
- CreateRoomDialog.tsx initializes canChangeEncryption=true, only queries server forcing, never applies forced value to isEncrypted, and submits true whenever locked. This causes flicker, incorrect displayed state, and incorrect submitted state for force-disable.
- createRoom.ts has no AllowedEncryptionSetting/checkUserIsAllowedToChangeEncryption helper; SDK doesServerForceEncryptionForPreset is async and represents server forced-on only. Higher-level policy should prefer this over .well-known forced-off and warn on conflict.
- WellKnownUtils.ts IE2EEWellKnown lacks force_disable; getE2EEWellKnown already resolves current and legacy keys. A strict === true check is needed in new utils/room/shouldForceDisableEncryption.ts.
- rooms.ts privateShouldBeEncrypted reads only default; force_disable must take precedence before default.
- Existing CreateRoomDialog tests cover defaults and server forced-on after promise resolution, but do not cover initialization flicker, forced-off, conflict, or submitted state under forced-off. createRoom tests do not cover permission helper.
