Implemented reserved system tag checks using normalized values from `meta.config.systemTags`. Topic creation, editing, queued posts, and the tag assignment API now pass the user ID to validation; unauthorized use throws **“You can not use this system tag.”** The tag availability check returns `false` for system tags.

Validation and tag writes are handled in [src/topics/tags.js](/app/src/topics/tags.js:65), with the availability check in [src/socket.io/topics/tags.js](/app/src/socket.io/topics/tags.js:10).

**Verification:** ESLint passed. The existing topic and category suites passed: **218 tests**. I started and shut down a temporary local Redis instance to run them.