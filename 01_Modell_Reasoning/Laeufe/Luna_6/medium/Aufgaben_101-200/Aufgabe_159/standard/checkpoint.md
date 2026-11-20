# Checkpoint

Issue: Correct ecosystem-specific package name parsing for PURLs.

Repository inspection found no `parsePkgName` function in the checked-out source. SBOM dependency components in `reporter/sbom/cyclonedx.go` currently use package names directly when creating PURLs. I am locating the PURL conversion code and package metadata types to determine the smallest compatible fix.
