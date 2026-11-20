Added a registration token entry view to InteractiveAuth for both `m.login.registration_token` and `org.matrix.msc3231.login.registration_token`. It displays the required field, help text, busy indicator and accessible error; Enter and the primary button submit the advertised type and token. The parent flow adds the session and preserves the completion callback’s extra argument.

The focused Jest suite passed (4 tests), as did ESLint, Prettier and `git diff --check`. Full type checking remains blocked by errors in unrelated SlidingSync files; it reported no errors in the changed files.

No delegation was used.