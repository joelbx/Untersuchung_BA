The backlink feature is absent from the checked-out code. The likely implementation points are:

- [src/topics/posts.js](/app/src/topics/posts.js) for the public `Topics.syncBacklinks(postData)` method and per-post sorted set.
- [src/posts/create.js](/app/src/posts/create.js) and [src/posts/edit.js](/app/src/posts/edit.js) to synchronize after a post is saved.
- [src/topics/events.js](/app/src/topics/events.js) to register `backlink` events and hide them from `Events.get()` when `topicBacklinks` is disabled. The existing [timeline renderer](/app/public/src/modules/helpers.js:225) already turns an event’s `href` into a link.
- [post settings](/app/src/views/admin/settings/post.tpl), [config defaults](/app/install/data/defaults.json), and the topic and admin language files for the toggle and localized text.

Synchronization should validate the post data, recognize site URLs and bare topic paths, ignore self-links and missing topics, diff references against `pid:{pid}:backlinks`, and log new events with the referencing post’s `pid` and author `uid`. One specification detail needs care: the interface defines the numeric return as **additions plus removals**, while an earlier example describes a current-state count. Removing obsolete *events* also needs an event ID mapping; the existing event API does not provide one from a post ID.

I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md). No project source or tests were changed.