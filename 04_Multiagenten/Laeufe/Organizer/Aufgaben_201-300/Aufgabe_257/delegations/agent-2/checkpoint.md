# tsh CLI implementation checkpoint

- Scope: tool/tsh/tsh.go and closely related existing tests. Left pre-existing lib/service/service.go changes untouched.
- Implemented: `Run(args, options...) error` applies options after parsing and dispatches errors; `main` handles error with `utils.FatalError`; `refuseArgs` and every handler defined in tsh.go now return errors without exiting; CLIConf and makeClient pass through mock SSO login.
- Added tests for option timing, parser error, and refused arguments.
- Verification: gofmt and git diff --check pass. `GOPROXY=off GOSUMDB=off go test ./tool/tsh -run 'TestParse|TestRefuse|TestReadCluster' -count=1` currently fails compilation because coordinator-owned client.SSOLoginFunc and client.Config.MockSSOLogin are not yet present.
- Out of assigned edit scope: database handlers and databaseLogin in tool/tsh/db.go still call utils.FatalError and return no error; coordinator must change them and update Run dispatch.
