Implemented Redis cache TLS configuration with CA file and inline CA support, optional certificate verification bypass, TLS 1.2 minimum, and the required conflicting-CA validation error. Added YAML fixtures and the `api/cachetls` integration matrix entry.

Relevant offline Go tests passed, and the integration harness compiled. The live TLS integration suite was not run locally.