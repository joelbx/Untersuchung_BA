Resolved the OSS leaf cluster access issue. Migration now downgrades the existing `admin` role in place, keeps users and trusted cluster mappings on `admin`, and skips an already labeled role. Legacy user creation also assigns `admin`.

The focused auth migration test and services role test passed; the `tctl` package compiled.