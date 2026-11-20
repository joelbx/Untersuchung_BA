Implemented selective SSE delivery. Request events now reach other sessions of the same user, excluding the originating client. Server generated events still broadcast to all subscribers.

The UI generates a UUID per page instance and sends it on its HTTP requests. The middleware stores it in an HttpOnly cookie and request context; the SSE URL carries it separately because browser tabs share cookies. I also updated event call sites, the diode API, logging, and cookie expiry constants.

Verification passed: the affected Go packages and `cmd`, all 42 UI tests, Prettier, and the production UI build. The build used Node’s legacy OpenSSL provider setting for the repository’s React tooling.