Task: Preserve lockfile paths through library scanning and vulnerability reporting.
Status: complete. Each lockfile is analyzed separately, findings carry their source path, duplicate CVEs retain all affected libraries, and reports resolve versions by path and name. Trivy/Fanal dependencies were advanced to cached versions exposing the required APIs.
Verification: GOPROXY=off GOSUMDB=off go test ./... passed; git diff --check passed.
