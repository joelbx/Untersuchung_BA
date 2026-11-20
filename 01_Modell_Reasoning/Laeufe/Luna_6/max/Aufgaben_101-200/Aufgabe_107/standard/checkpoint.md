# Checkpoint

## Objective
Fix stale entries in the mail elements bypass filter when marking elements read or unread.

## Findings
- The optimistic mark-as hook supplies updated element data and already has the requested status.
- `ElementsState.params.filter.Unread` uses `1` for unread and `0` for read.
- The reducer previously added IDs whenever `bypass` was true and had no removal path.

## Changes made
- Added optional `markAsStatus` to optimistic update payloads and passed it from the mark-as hook.
- Added `getElementsToBypassFilter` to select elements for add/remove based on the unread filter and status.
- Updated the reducer to add eligible IDs without duplicates and remove matching IDs when bypass is no longer needed.

## Verification
- Existing `Mailbox.elements.test.tsx`: 12 tests passed.
- `yarn workspace proton-mail check-types --pretty false`: passed.
- Targeted ESLint: passed.
- Targeted Prettier check and `git diff --check`: passed.
