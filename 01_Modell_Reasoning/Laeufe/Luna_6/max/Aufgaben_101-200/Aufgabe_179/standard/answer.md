Implemented persistent RemoteCluster status and heartbeat updates. Tunnel upserts now record the latest heartbeat; deletes refresh status while retaining the highest recorded heartbeat. With no connections, clusters are marked Offline without clearing that heartbeat.

Added `Presence.UpdateRemoteCluster` with expiry and resource ID preservation, plus the authenticated API and client method required by the interface.

**Verification:** Local presence, cache, and services tests passed. Filtered auth tunnel and RemoteCluster CRUD tests passed. Full auth runs hit `PasswordSuite.TestTiming` twice, exceeding its 10% timing threshold by 10.79% and 12.05%.