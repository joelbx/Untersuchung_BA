Fixed the Direct Dial address in `/app`. Inventory streams now expose the peer address, and SSH heartbeats use its host when the node reports a wildcard or local address, preserving the node’s original port for `UpsertNode`.

The relevant `lib/inventory` and `api/client` tests passed offline, as did `git diff --check`.