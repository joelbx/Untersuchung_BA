Implemented square album covers in the grid. The grid now requests `square=true`; the artwork API returns centered square PNGs for that option, including placeholders, and uses separate cache keys for square and regular versions. Regular cover requests keep their existing behavior.

The relevant Go tests, repository-wide Go build check, frontend lint and formatting checks all passed.

I did not add `internal/storage/fs/oci/source.go`: this Navidrome checkout has no OCI storage tree or the types that interface requires.