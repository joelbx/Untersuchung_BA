Fixed authentication startup so JWT-only configurations with Local, Git, OCI, or Object flag storage do not connect to a database. Database requirements are now explicit for each authentication method, and cleanup skips disabled methods and JWT.

The targeted configuration, startup, and cleanup tests passed.