Implemented HEIC/HEIF and JXL support for macOS/iOS Safari 17+, added the JXL MIME type and extension mapping, and simplified MIME detection to use the filename extension before falling back to `File.type`.

Prettier and `git diff --check` passed. Type checks and drive-store lint ran but reported unrelated existing errors in the workspace.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)