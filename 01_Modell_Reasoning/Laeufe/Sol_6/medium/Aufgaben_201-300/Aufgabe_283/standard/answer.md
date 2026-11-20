Added `isFromProton(element: Element): boolean`. It returns `true` only when `IsProton === 1` and works for messages and conversations. The existing column-list verified badge now uses that check and has a “Verified message” tooltip.

Verification passed: 22 element helper tests, the mail TypeScript check, and `git diff --check`.