I updated the installed package and repoquery parsers to preserve empty release fields and build package versions with the release suffix when present.

`go test ./scanner` is still running and has not returned a result yet. The source RPM filename and update candidate parsing requirements remain unresolved.