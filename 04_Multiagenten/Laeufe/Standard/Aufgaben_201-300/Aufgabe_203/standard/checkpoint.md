Task: Improve accessible names and external-link cues in Element Web.
Plan: inspect current links and styles, add shared ExternalLink, update settings and room share, add localization, run relevant existing tests.
Status: implementation complete. Added ExternalLink and stylesheet; converted new-tab links in settings; named share-dialog links; added i18n strings.
Verification: settings Jest suites 3/3 passed after generating ignored src/component-index.js; focused ESLint, Stylelint, and git diff --check passed. Full TypeScript check remains blocked by six existing ThreadEvent errors in ThreadView.tsx and ThreadNotificationState.ts.
