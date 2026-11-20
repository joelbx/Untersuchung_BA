Task: Support HEIC/JXL thumbnail and preview generation on macOS/iOS Safari 17+.
Status: implementation complete.
Changes: added image/jxl enum and extension mapping; added Safari/OS/version gates for HEIC and JXL in isSupportedImage; simplified MIME detection in both Drive source trees to prefer a specific File.type and otherwise resolve the extension.
Verification: focused MIME and capability Jest tests passed (12); existing media Jest tests passed (6); focused ESLint and Prettier checks passed; git diff --check passed. Shared and drive-store TypeScript checks fail on unrelated existing crypto/OpenPGP type conflict and drive-store missing symbols/modules.
