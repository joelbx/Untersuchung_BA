Updated collection build and install to preserve symlinks whose targets stay within the collection, avoid traversing symlinked directories in the manifest, and store external file symlinks as regular files. Tar helpers now return the member and readable stream, and extraction validates paths before restoring symlinks.

Verification: 103 relevant unit tests passed; `git diff --check` passed.