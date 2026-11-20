Implemented durable RemoteCluster status and heartbeat updates.

- Added `UpdateRemoteCluster` to the Presence interface, local storage, and auth API/client. It writes the serialized cluster to `remoteClusters/<name>` and preserves expiry.
- Status refresh now reports Offline when no tunnels remain, Online when any tunnel exists, and only advances the stored heartbeat to a newer UTC timestamp.
- The local presence tests passed. The auth API test passed. The earlier full auth run had a timing-sensitive failure in `PasswordSuite.TestTiming`; its other 81 tests passed.