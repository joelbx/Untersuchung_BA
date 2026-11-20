The failure is in [getEntryComponentForLoginType](/app/src/components/views/auth/InteractiveAuthEntryComponents.tsx): neither registration token identifier has a case, so both reach `FallbackAuthEntry`. There is no `RegistrationTokenAuthEntry` view.

The installed SDK already defines both identifiers and a `token` field. Its `submitAuthDict` adds the session, and [InteractiveAuth](/app/src/components/structures/InteractiveAuth.tsx) already forwards the advertised stage type and calls `onAuthFinished` with the server response and the `clientSecret`/`emailSid` object on success.

The likely fix is to add the dedicated view and route both identifiers to it, submitting exactly `{ type: props.loginType, token }`. Coverage should check the specified field, help text, button, Enter submission, busy and error states, and completion for both identifiers. Existing tests cover a password flow but no token flow. This diagnosis is based on local code; it has not been validated against a homeserver.

I updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). I did not edit source or tests because the assigned fault-localization role explicitly prohibits those changes.