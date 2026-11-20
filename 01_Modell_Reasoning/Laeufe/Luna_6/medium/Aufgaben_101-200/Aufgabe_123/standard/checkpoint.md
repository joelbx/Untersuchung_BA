# Checkpoint

Implemented notification string sanitization with DOMPurify, made sanitized anchors open in a new tab with `rel="noopener noreferrer"`, and changed non-success deduplication to use the explicit key, string text, or notification identifier fallback. Success notifications are excluded from deduplication; React element content remains supported.

Verification: `yarn workspace @proton/components check-types --pretty false` completed without reported errors. No existing tests specifically cover the notification manager or renderer.
