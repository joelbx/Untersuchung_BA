Updated `ansible-galaxy install -r` to install roles and collections in one run when using default paths. Custom role paths and explicit subcommands now skip the other type with the requested messages. Empty requirements files skip installation, and role dependency handling respects force options.

Added CLI coverage for these cases. The relevant local suite passed: **132 tests**.