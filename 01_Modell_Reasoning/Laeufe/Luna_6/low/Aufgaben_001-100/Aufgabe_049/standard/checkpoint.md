# Checkpoint

Implemented the email confirmation key model (`confirm:byUid:<uid>` plus `confirm:<code>` with explicit millisecond `expires`), pending/expiry helpers, pending resend protection with `force`, same-address rejection, fallback email lookup, ACP force validation/resend behavior, four-state ACP status text, and confirmation cleanup during account deletion and successful validation.

Verification: ESLint passes for all four modified JavaScript files; `git diff --check` passes. Focused existing Mocha tests (`test/user.js --grep 'email|confirm'`) could not initialize because Redis at `127.0.0.1:6379` refused the connection, so no tests ran.

Files changed: `src/user/email.js`, `src/socket.io/admin/user.js`, `src/user/delete.js`, `src/controllers/admin/users.js`, `src/views/admin/manage/users.tpl`.
