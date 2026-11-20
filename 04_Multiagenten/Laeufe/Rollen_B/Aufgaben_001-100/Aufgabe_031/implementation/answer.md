Fixed configuration loading so `Load("")` starts with defaults and applies `FLIPT_` environment overrides. The CLI now uses that loader when no config file is found.

Tests cover default values and environment precedence with and without a file. The config tests passed, and the CLI package compiled successfully.