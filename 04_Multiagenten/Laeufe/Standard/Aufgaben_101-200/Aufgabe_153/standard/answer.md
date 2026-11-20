Updated the Drive member view so members, internal invitations, and external invitations are stored and displayed by share ID. Writes to one share now leave other shares’ data intact. Added `getExistingEmails` and regression tests for share isolation.

The package type check and 8 relevant tests pass.