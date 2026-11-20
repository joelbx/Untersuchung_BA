Added a `user_props` table and a context-scoped `UserPropsRepository`. The migration moves existing Last.fm session keys into the new table, and Last.fm now uses the defined `sessionKeyProperty` key without constructing user-prefixed keys. Property error logs include the request ID when available.

Repository isolation, migration, and full Go tests passed.