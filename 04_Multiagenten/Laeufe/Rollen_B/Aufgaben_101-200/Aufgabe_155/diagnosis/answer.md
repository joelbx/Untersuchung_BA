The fault spans configuration, scanning, and reporting:

- [config/config.go](/app/config/config.go:1091) and [models/scanresults.go](/app/models/scanresults.go:447) lack `Digest`; `config.Image` also lacks `GetFullName()`.
- [config/tomlloader.go](/app/config/tomlloader.go:297) requires a tag and never checks for a tag–digest conflict.
- [scan/container.go](/app/scan/container.go:108) builds `name:tag` for scanning, and [scan/base.go](/app/scan/base.go:419) copies only the tag into results.
- [scan/serverapi.go](/app/scan/serverapi.go:503) embeds the tag in the per-image server name and formats an integer index with `%s`.
- [report/report.go](/app/report/report.go:533) builds UUID identifiers as `name:tag@server`.

The fix should validate exactly one of tag or digest using the specified errors, use `name:tag` or `name@digest` throughout scanning and reporting, and set per-image server names to `<index>@<originalServerName>`. **Uncertainty:** local and cloud report filenames also derive from `ServerName`; they should be checked for distinct, consistent image results after that naming change. Existing tests contain no digest-specific coverage.

I updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project source or tests were edited because this pass was restricted to fault localization.