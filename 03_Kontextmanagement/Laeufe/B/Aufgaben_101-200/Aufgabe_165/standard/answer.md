Implemented `.well-known` `force_disable` support and updated the room creation dialog to show and submit the enforced encryption state.

Targeted tests passed: **25/25**. ESLint and Prettier passed. Type checking remains blocked by an error in unchanged [Unread.ts](/app/src/Unread.ts:167).