Added JXL MIME detection and enabled HEIC, HEIF, and JXL previews on macOS and iOS Safari 17+. Both upload parsers now use a specific `File.type` when available and fall back to the file extension, without reading file content.

All 10 tests in three relevant Jest suites pass. Both workspace type checks remain blocked by errors outside the edited files.