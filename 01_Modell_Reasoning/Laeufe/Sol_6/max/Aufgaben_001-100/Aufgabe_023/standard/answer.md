JWT-only authentication now uses an in-memory authentication store, so it does not call `getDB` with Local, Git, OCI, or Object flag storage. Each authentication method explicitly declares `RequiresDatabase`; startup and cleanup use that value for enabled methods.

The configuration, startup, and cleanup package tests passed. The JWT startup test also passed in isolation.