# Backlink feature checkpoint

- Added `Topics.syncBacklinks(postData)` to scan same-site and bare topic links, reconcile `pid:{pid}:backlinks`, and add/remove topic backlink events. It returns the count of added and removed associations and rejects invalid post data.
- Wired synchronization into post creation and editing. Added the `backlink` timeline event type, admin toggle (`topicBacklinks`, disabled by default), and English localization.
- Added integration coverage for creation, edit removal/addition, invalid and duplicate references, and visibility.
- Verified with local Redis: `mocha test/topicEvents.js test/posts.js --reporter dot` (110 passing), ESLint for changed JS files, and `git diff --check`.
