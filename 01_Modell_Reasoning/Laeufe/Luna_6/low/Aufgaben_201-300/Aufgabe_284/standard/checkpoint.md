# Checkpoint

Task: resolve redundant localsite storage and cache construction in reversetunnel.Server.

Plan: inspect server/localSite implementation and existing tests; refactor to one localSite that reuses server access point and clients; update affected callers and run relevant existing tests.
