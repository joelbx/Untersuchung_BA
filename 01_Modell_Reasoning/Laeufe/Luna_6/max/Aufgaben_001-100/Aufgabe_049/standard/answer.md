Implemented the confirmation key mapping, explicit expiry, email fallback, pending and expiry helpers, and forced resend behavior in [email.js](/app/src/user/email.js:28). User deletion now removes the mapping and its confirmation object in [delete.js](/app/src/user/delete.js:107).

The ACP user list now shows all four email states and displays a pending address when the profile has no email: [users.js](/app/src/controllers/admin/users.js:184), [users.tpl](/app/src/views/admin/manage/users.tpl:111).

**Verification:** lint, syntax checks, language JSON parsing, and `git diff --check` passed. The user suite reported 133 passing and one failure: an existing test expects a resend while a non-expired confirmation is pending, which the new requirement disallows unless forced.