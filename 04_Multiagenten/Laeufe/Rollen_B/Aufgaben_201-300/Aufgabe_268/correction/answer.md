Updated `start_detached` to report the capitalized process name, quoted command, failure type, and error detail. On non-Windows systems, it also adds the executable hint when the command is missing or cannot be executed, including when Qt reports only “Unknown error.”

The updated unit suite passed (32 tests), the reviewer’s end-to-end startup scenario passed, and `git diff --check` passed.