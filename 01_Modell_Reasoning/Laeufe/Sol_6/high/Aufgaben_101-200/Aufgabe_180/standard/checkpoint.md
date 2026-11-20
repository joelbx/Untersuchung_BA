# Checkpoint

Task: update OS EOL data and Windows KB rollup mappings, preserve existing entries, and verify kernel-version detection with existing tests.

Status: EOL timelines and macOS 11/15 updated; Windows 19045, 22621, 22631, and 20348 rollups extended with named literals. Existing KB expectations updated and focused boundary tests added. Static audit confirms all previous entries remain in place and appended revisions increase. Focused config and scanner Go tests pass with network module fetching disabled.
