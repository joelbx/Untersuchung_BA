Added a `user_props` migration that moves existing Last.fm session keys, plus a context-scoped `UserPropsRepository` exposed through `DataStore`. Last.fm now uses the `sessionKeyProperty` key without constructing user-prefixed keys, and property error logs include the request ID when available.

`GOPROXY=off GOSUMDB=off go test ./... -count=1` passed.