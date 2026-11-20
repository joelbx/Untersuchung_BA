Updated `VoiceBroadcastPreRecordingPip` so “Go live” renders as a native button, becomes disabled immediately on activation, and ignores further activations until `start()` settles. Device selection still closes the menu and updates the header label.

The focused suite passes: 7 tests. The repository typecheck remains blocked by existing `MatrixClient` type errors outside these changes.