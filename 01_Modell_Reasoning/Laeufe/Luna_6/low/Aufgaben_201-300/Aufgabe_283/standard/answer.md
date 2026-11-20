Added `isFromProton(element: Element)` to [elements.ts](/app/applications/mail/src/app/helpers/elements.ts). It returns `true` only when `IsProton` equals `1`, using the same logic for messages and conversations.

Added tests for both element types with `IsProton` values `1` and `0`. The existing `elements.test.ts` suite passed.