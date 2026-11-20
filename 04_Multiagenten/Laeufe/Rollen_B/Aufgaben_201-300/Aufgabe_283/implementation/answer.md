Added `isFromProton(element)` in [elements.ts](/app/applications/mail/src/app/helpers/elements.ts). It returns `true` only when `IsProton === 1`. I also added the optional field to the message, conversation, and encrypted search message types.

The focused tests pass (22/22), and the mail type check passes.