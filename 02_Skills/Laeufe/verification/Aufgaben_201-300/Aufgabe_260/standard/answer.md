Implemented selective SSE delivery. The UI sends a per-window client UUID; middleware stores it in an HttpOnly cookie and request context. The broker now sends request events only to other clients of the same user, while background events broadcast to all clients.

Verification passed: the affected Go packages, 41 UI tests, UI lint and formatting, and `git diff --check`.