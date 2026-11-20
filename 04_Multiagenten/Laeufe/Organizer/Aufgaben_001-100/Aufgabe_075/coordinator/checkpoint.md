Task: move user-specific properties to user_props; expose context-scoped repository; refactor Last.fm.
Status: implemented and verified.
Changes: migration creates user_props and moves/deletes legacy Last.fm keys; model/DataStore/SQLStore expose UserProps; SQL repository scopes Put/Get/Delete to request user; Last.fm uses sessionKeyProperty and callback attaches user context; mocks and tests updated.
Validation: go test ./... passed; git diff --check passed. No delegation used.
