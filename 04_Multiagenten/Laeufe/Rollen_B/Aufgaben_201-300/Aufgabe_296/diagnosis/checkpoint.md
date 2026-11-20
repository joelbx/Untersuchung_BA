Progress: fault localization complete; project source and tests untouched.
- src/user/invite.js stores a single token at invitation:email:<email>, requires query.email in verifyInvitation, reads groups by email, and deletes only that email key. It has no confirmIfInviteEmailIsUsed.
- public/src/client/register.js has commented-out URL token population; the rendered register.tpl already has a hidden token input.
- src/controllers/authentication.js verifies submitted token, but invite post-registration group join and cleanup are commented out. src/user/email.js exposes email.confirmByUid(uid).
- Existing test/user.js invitation tests read invitation:email:<email> and cover email-bearing registration; token-only and multi-token cleanup coverage is absent.
- Likely fix spans token-keyed invitation storage/lookup and cleanup in src/user/invite.js, URL token population in public/src/client/register.js, and post-create actions in src/controllers/authentication.js. Account for token without email, matching versus nonmatching entered email, group join, and all associated token/inviter reference cleanup.
