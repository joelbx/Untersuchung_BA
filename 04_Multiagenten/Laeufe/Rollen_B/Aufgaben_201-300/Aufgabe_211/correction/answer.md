Fixed post purge so that, when an upload has no remaining post references and preservation is disabled, it deletes both the original file and its `-resized` image. The upload test now checks that both files remain while another post references the image.

The reviewer’s exact Mocha command passed (56 tests), the flagged ESLint command passed, and `git diff --check` passed.