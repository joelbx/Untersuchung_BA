Resolved the nullable field issue in `/app`. Album and artist update times, share timestamps, and album `image_files` now load safely when the database value is null. Added `gg.P` and `gg.V` and regression tests.

The affected package tests pass. The full suite still has four unrelated TagLib test failures.