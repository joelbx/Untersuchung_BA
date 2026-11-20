Implemented disabled flag handling for batch evaluation. Disabled flags now return a typed `ErrDisabled`, appear in the response in input order with `value: "disabled"`, a timestamp, and their own duration. The outer response retains the total batch duration.

Migrated RPC empty results and timestamp handling to `emptypb` and `timestamppb`, including database timestamp helpers.

Validation passed: `GOPROXY=off go test ./server ./storage/db/... ./rpc`. `git diff --check` also passed.