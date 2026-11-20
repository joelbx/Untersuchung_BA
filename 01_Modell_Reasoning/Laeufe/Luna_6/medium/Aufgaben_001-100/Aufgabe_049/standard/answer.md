Implemented the email validation changes across [email.js](/app/src/user/email.js), [users.js](/app/src/controllers/admin/users.js), [delete.js](/app/src/user/delete.js), [profile.js](/app/src/user/profile.js), and the ACP user table.

Confirmation records now use `confirm:byUid:<uid>` and `confirm:<code>` with an explicit millisecond `expires` value. Added `isValidationPending`, `expireValidation`, and `getEmailForValidation`; updated resend, admin validation, and deletion flows; and added the four email status labels to the ACP.

JavaScript syntax checks and `git diff --check` passed. The focused user tests could not run because Redis was unavailable at `127.0.0.1:6379`.