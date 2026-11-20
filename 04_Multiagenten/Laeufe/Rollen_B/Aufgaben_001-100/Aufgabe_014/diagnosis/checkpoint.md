Fault localization complete. No project source or tests changed.
Notifications: public/src/client/header/notifications.js loads on show and initial open via AMD require, passing only list; public/src/modules/notifications.js loadNotifications toggles global notifications component. Async responses can apply after a later open/close.
Modal selectors: fork.js and move.js cache parsed modal and initialize categorySelector, but fork-topic.tpl and move-topic.tpl import selector without dropup. Set class on cached selector before init.
Quick search: public/src/modules/search.js uses blur timeout and mousedownOnResults, and action:ajaxify.end only marks ajaxified; stale results persist.
Storage: mongo/hash.js getObjectsFields uses raw fields against normalized keys, deleteObjectFields filters before normalization; redis/hash.js passes raw fields in several commands and filters raw values.
Other: emailer.js sendViaFallback concatenates from string; install.js completeConfigSetup dereferences install.values; routes/index.js post redirects bypass tryRoute; admin/manage/users.tpl menus unbounded; merge-topic.tpl quick search menu has no width; partials/chats/recent_room.tpl uses div wrapper despite click navigation.
Existing test/database/hash.js covers empty/undefined field cases but not normalized numeric/dotted fields. No tests run because analysis-only role.
