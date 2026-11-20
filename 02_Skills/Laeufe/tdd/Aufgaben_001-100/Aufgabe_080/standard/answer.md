Implemented the album grid cover-art fix. Square requests now return a centered PNG on a square canvas, use a distinct cache key, and flow through the backend and frontend. Non-square requests keep their image shape and format.

The focused Go tests and all 46 UI tests pass. The full Go suite has two unrelated failures in TagLib’s m4a gain-tag tests, which receive duplicate replay-gain values; details are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).

The requested OCI `Source` interface was not added: this Navidrome checkout has none of its required OCI packages or types.