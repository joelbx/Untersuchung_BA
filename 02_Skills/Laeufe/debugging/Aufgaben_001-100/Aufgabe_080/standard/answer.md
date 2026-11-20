Updated AlbumGrid to request square covers. The artwork pipeline now centers non-square images on a square canvas, returns PNG for square requests, and uses separate cache keys. Requests without `square=true` retain their original shape and format.

Verification passed: targeted Go tests, a repository-wide Go compile check, 46 UI tests, formatting, and lint.

The requested OCI `Source` interface was not added: its path and referenced types do not exist in this repository and are unrelated to the AlbumGrid issue.