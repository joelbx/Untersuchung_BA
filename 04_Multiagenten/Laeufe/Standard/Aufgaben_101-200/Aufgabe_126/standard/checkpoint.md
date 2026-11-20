# Checkpoint

Task: preserve assistant HTML formatting, scope embedded URLs by messageID, and repair nested lists.
Status: implementation complete. Composer identity flows through preparation, preview, and insertion. URL placeholders store messageID and formatting attributes; restoration drops foreign or invented elements while retaining link text. Nested lists are normalized and assistant Markdown conversion enables list rules. Focused Jest tests passed (7 tests). Package type check reports one pre-existing error in packages/crypto/lib/worker/api.ts from duplicate OpenPGP types; no errors in edited files.
