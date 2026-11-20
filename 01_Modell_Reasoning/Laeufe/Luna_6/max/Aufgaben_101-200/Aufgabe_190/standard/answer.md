Implemented preview mode for both import endpoints. Preview runs the matched and new-record paths without saving, uploading covers, or writing metadata back to Archive.org, and returns `preview`, planned record edits, simulated UUID keys, and cover acceptance.

Added case-insensitive cover host validation, normalized author matching, and edition construction for descriptions and languages. Updated the existing cover test to use an allowlisted Amazon host.

**Verification:** 128 relevant tests passed; Ruff checks passed.