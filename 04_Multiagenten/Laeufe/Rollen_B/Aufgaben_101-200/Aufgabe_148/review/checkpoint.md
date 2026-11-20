VERDICT: ACCEPT
Reviewed the applied patch in lib/multiplexer and lib/sshutils. Prefix detection routes to SSH, clientAddr is exposed through RemoteAddr before server connection limiting, and the SSH wrapper consumes the NUL-terminated metadata while preserving standard SSH reads. No concrete code defect found.
Tests executed successfully:
- go test ./lib/multiplexer -run 'TestDetectTeleportProxySSH|TestMux' -count=1
- go test ./lib/sshutils -run 'TestConnectionWrapperFragmentedProxyHeader|TestStartStop' -count=1
- go test ./lib/multiplexer ./lib/sshutils -count=1
- git diff --check
