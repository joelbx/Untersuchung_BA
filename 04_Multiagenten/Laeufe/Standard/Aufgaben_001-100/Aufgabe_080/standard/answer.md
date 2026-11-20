Updated the artwork API and cache keys to distinguish square covers. Square requests now return a centered PNG with equal width and height; the album grid requests that version. Existing non-square requests retain their aspect ratio and format.

The artwork and server tests pass, and the changed frontend files pass Prettier. The full Go suite has two unrelated TagLib AAC gain tag failures caused by duplicate values.

I did not create the requested OCI `Source`: this Navidrome checkout has no OCI storage packages for it to use.