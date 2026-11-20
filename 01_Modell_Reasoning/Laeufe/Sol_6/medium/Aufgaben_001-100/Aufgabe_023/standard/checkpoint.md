# Checkpoint

Task: avoid database initialization for JWT-only authentication with non-database flag storage.
Status: complete. Authentication database requirements are explicit; startup uses memory storage for JWT-only non-database backends; cleanup excludes JWT and disabled methods.
Verification: targeted Go tests passed for configuration, JWT startup on Local/Git/OCI/Object storage, existing gRPC startup, and authentication cleanup. git diff --check passed.
