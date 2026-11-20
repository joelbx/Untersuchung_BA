Implemented IDN handling in the checked-out repository. `punycodeUrl` converts Unicode hostnames to ASCII while preserving URL components and removing a trailing pathname slash. `useLinkHandler` now applies that conversion to external links and shows an error when a link URL is missing or cannot be parsed.

The URL tests, component type check, targeted lint, and `git diff --check` all passed.