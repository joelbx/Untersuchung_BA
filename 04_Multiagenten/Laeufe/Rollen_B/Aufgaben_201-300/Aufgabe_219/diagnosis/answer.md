The likely fix spans three places:

- [checker.go](/app/internal/server/audit/checker.go:17) omits `token` from both its resource map and `*` expansion. It therefore rejects explicit token events and excludes them from wildcard selections.
- [grpc.go](/app/internal/cmd/grpc.go:282) initializes authentication before creating the audit checker. Startup needs the checker’s `Check("token:deleted")` result, with audit sinks enabled, to reach the authentication server.
- [auth.go](/app/internal/cmd/auth.go:78) currently passes only `cfg.Audit.Enabled()`. [server.go](/app/internal/server/auth/server.go:134) already emits a token deletion event when that boolean is true; it needs the event-specific value. The middleware already constructs token creation events.

Coverage should verify `token:created` and `token:deleted` for explicit and matching wildcard configurations, and verify that deletion logging stays off when only other events are selected. One uncertainty is whether deletion audit events should be emitted after a successful store deletion; the current code adds the event before deleting.

I updated the required checkpoint note. This pass was limited to fault localization, so project source and tests were not changed or run.