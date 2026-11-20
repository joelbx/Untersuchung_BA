# U2F multi-device authentication

Status: implementation and focused tests complete. U2F sign requests now include every registered key, expose legacy top-level fields, and use one shared browser nonce. Auth HTTP client, CLI login, and web flow consume the new format with legacy fallback. The bundled web UI is adapted at serve time to pass all challenges to the browser U2F API. `tsh mfa` remains hidden in help.

Verified: auth multi-device test, existing MFA device management test, combined web U2F login/password tests, and client and tsh package builds. All passed.
