# Checkpoint

Implemented share-keyed invitation and member stores in both mirrored Drive trees. Getters return empty arrays for missing share IDs; setters and updates touch only the selected share. The Zustand member view now reads and mutates data for its resolved share ID.

Added and exported `getExistingEmails` to combine member, internal invitation, and external invitation email addresses.

Validation: `yarn workspace @proton/drive-store check-types` passed. `git diff --check` passed. No existing tests directly cover these Zustand share stores.
