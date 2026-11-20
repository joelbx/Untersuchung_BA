Updated collection build and install to preserve internal file and directory symlinks, copy external file link content into the artifact, and validate link targets before extraction. Tar extract helpers now return the `TarInfo` alongside the stream. Added round trip and unsafe link tests.

Verification: all 61 collection unit tests passed, and `git diff --check` passed.