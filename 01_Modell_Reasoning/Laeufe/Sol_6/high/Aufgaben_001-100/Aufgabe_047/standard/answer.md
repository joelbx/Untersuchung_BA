Added `SetSeed` at the package and `Hasher` method levels. The hasher now initializes missing per-ID seeds, supports reseeding and restoring a prior seed, and synchronizes seed access. Added tests for those behaviors.

`go test ./utils/hasher` and `go test ./db ./persistence` pass.

Because `maphash` uses a process-local seed, restored values reproduce hashes within a process, including across `Hasher` instances; they are not guaranteed to match after a restart.