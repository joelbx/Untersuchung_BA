The no-file startup path is the direct cause: [buildConfig](/app/cmd/flipt/main.go:186) keeps `config.Default()` when no file is found, bypassing the environment handling in [config.Load](/app/internal/config/config.go:63).

`Load("")` also needs attention: it unconditionally calls `ReadInConfig()` and has no explicit path for loading defaults without a file. The existing [Load tests](/app/internal/config/config_test.go:744) pass a YAML path even in their environment-variable cases, so they do not establish the required empty-path behavior.

The fix should make `Load("")` produce defaults with environment overrides, then have the CLI use that result when no file is found. It should preserve environment precedence for file-based loads and cover `FLIPT_LOG_LEVEL` and integer `FLIPT_SERVER_HTTP_PORT`. One naming detail needs care: the current key is `server.http_port`; the issue calls it `server.http.port`, and both spellings collapse to the same environment name under dot-to-underscore replacement.

This diagnosis is from code inspection; I did not run tests or modify project source or tests, as required by the specialist instructions.