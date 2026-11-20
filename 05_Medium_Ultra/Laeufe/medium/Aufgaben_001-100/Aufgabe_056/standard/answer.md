Added `image/jxl` and its extension mapping, enabled HEIC/HEIF and JXL previews on macOS and iOS Safari 17+, and simplified MIME detection in both Drive upload parsers to use `File.type` with an extension fallback.

The existing thumbnail test, Prettier, and `git diff --check` passed. Type checks are blocked by errors in unchanged crypto and Drive Store files; targeted ESLint ran out of memory.