Added [isFromProton](/app/applications/mail/src/app/helpers/elements.ts:44). It returns `true` only when a mail element’s `IsProton` value is `1`, using the same check for messages and conversations.

The existing 19 helper tests and the mail type check passed.