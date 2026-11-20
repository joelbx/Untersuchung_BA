Fixed JSON loading for both saved `listenPorts` formats. String entries populate `ListenPorts`; object entries populate `ListenPortStats`, preserving saved reachability data. Added regression tests.

The reviewer’s exact command, `GOPROXY=off GOSUMDB=off go test ./models ./scan ./report`, passed.