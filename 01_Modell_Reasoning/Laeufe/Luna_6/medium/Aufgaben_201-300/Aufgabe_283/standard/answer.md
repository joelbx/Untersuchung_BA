Added `isFromProton` in [elements.ts](/app/applications/mail/src/app/helpers/elements.ts). It returns `true` only when `IsProton === 1`, for both Message and Conversation elements.

Added tests for `IsProton` values 1 and 0 on both types. The existing helper test suite passed.