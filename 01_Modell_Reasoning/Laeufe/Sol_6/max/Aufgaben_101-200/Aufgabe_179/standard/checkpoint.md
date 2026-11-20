# RemoteCluster status and heartbeat fix

Completed. Added Presence.UpdateRemoteCluster with backend update and expiry preservation, wired the auth client/API method, and changed auth reads to persist status while retaining the greatest heartbeat. Added lifecycle and expiry tests. Relevant existing local and auth CRUD tests pass (3 local, 3 auth).
