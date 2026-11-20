Updated the repository so Debian and Red Hat use a shared `pkgPs` path to associate processes with packages. Red Hat now resolves RPM owners by package name in both process scanning and `needsRestarting`, avoiding the FQPN mismatch warning. RPM parsing ignores the three specified file diagnostics and returns an error for malformed lines.

`go test ./scan ./models` passed with network access disabled.

**Limit:** the package inventory still stores one version and architecture per package name. This fixes process lookup against that inventory, but does not add separate reporting for every installed variant.