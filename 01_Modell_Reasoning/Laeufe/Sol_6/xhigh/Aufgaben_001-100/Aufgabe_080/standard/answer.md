Implemented the AlbumGrid fix. Square requests now produce centered, square PNG artwork with a separate cache key, and AlbumGrid requests that version. Other artwork requests keep their existing behavior.

The relevant Go tests, frontend URL test, lint, and formatting checks pass.

I did not add the requested OCI `Source`: this Navidrome checkout has no OCI storage subsystem or the types its interface requires. That requirement needs the matching repository.