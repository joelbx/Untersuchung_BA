# Checkpoint

Task: Add Safari 17+ HEIC/JXL image support and simplify MIME detection.
Status: Implemented in shared MIME helpers/constants and both Drive parser copies.
Validation: Existing getMediaInfo test passes; Prettier and git diff --check pass. Shared and Drive Store type checks fail on existing crypto/OpenPGP and Drive Store errors outside edited files. Targeted ESLint exceeded the default Node heap.
