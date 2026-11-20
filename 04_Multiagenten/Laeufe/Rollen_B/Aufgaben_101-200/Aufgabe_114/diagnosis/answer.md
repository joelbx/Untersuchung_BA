I could not edit the repository to resolve this issue: my assigned role for this run is fault localization only, with project source and tests left untouched.

The likely change sites are:

- [model/album.go](/app/model/album.go:41) and [scanner/refresher.go](/app/scanner/refresher.go:97): albums store image paths, but not their media directories. [MediaFiles.Dirs](/app/model/mediafile.go:87) already computes unique directories; the scanner currently uses them only to collect images.
- [core/artwork/reader_artist.go](/app/core/artwork/reader_artist.go:23): the artist reader gathers album image lists but computes no artist base folder. Its lookup starts with those lists, then tries the URL and placeholder.
- [core/artwork/sources.go](/app/core/artwork/sources.go:22): the shared lookup loop traces each attempt without its duration.

A fix should make album media directories available to the artist reader, derive a base folder, try `artist.*` there first, preserve the existing fallbacks, and time every lookup attempt. The intended rule for choosing a base folder when an artist’s albums span multiple directory trees is unclear from the code and issue text.