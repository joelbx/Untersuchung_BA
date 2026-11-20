Updated `UserPropsRepository` and its mock so every read and write requires a `userId`. LastFM now passes the user ID through session key lookup, persistence, unlinking, now playing, and scrobbling. Added a two user isolation test.

`go test ./...` passed.