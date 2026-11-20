Task: Fix AlbumGrid shaking with non-square artwork and implement requested interfaces where applicable.
Status: Artwork API, resize path, cache keys, endpoint parameters, grid URL, and tests updated. Targeted Go tests pass. Full Go suite fails only in two unrelated TagLib AAC gain tag cases (duplicate values). Frontend Prettier check passes.
Repository finding: OCI snapshot source interfaces refer to packages absent from this Navidrome checkout and are unrelated to the album artwork issue.
Constraints: Local repository and existing tests only; preserve git history, index, and harness configuration.
