Implemented `user_props` with a migration that preserves existing LastFM session keys, added a context scoped `UserPropsRepository` through `DataStore`, and moved LastFM session handling to the `sessionKeyProperty` key. Property error logs now include the request ID when available.

The relevant persistence, LastFM, scrobbler, and server tests passed.