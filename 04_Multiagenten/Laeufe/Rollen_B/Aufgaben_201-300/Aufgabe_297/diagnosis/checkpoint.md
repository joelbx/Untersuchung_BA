# Fault-localization progress

Inspected local source and existing tests. No project source or tests changed.

Findings:
- No ReverseProxyWhitelist, ReverseProxyUserHeader, validateIPAgainstList, or handleLoginFromHeaders exists in this checkout. conf/configuration.go defines options/defaults.
- server/app/serve_index.go assembles frontend config and logs it; server/app/auth.go has password login and token creation. server/app/app.go mounts serveIndex on UI root.
- server/server.go applies Chi RealIP before app routing. Any whitelist based on r.RemoteAddr must account for forwarded-header trust.
- ui/src/config.js parses injected config; ui/src/authProvider.js stores standard login fields including Subsonic credentials; ui/src/App.js checks localStorage token.
- log/redactrus.go Fire only redacts top-level strings and calls reflect.TypeOf(v).Kind() without nil guard. Nested maps containing auth payload can leak in debug logs.
- Existing tests cover ordinary login and config values, not reverse proxy auth or map redaction.

Uncertainty: requirement both says header user must exist and says create missing user on first login; likely intended create on first trusted login, then authenticate. Unix socket handling is specified but server.Run currently uses http.ListenAndServe.
