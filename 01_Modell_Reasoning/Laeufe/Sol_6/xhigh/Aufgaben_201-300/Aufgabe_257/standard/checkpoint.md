# Checkpoint

Resolved: tsh Run accepts post-parse configuration options and returns command errors; all tsh handlers and refuseArgs return errors. CLIConf.mockSSOLogin reaches client.Config.MockSSOLogin, and TeleportClient.ssoLogin invokes an injected SSOLoginFunc.

Auth and proxy services now retain OS-assigned listener addresses in their config, logging, and dependent proxy settings. proxyListeners owns and closes the SSH listener.

Verification: `GOPROXY=off GOSUMDB=off go test ./tool/tsh ./lib/client ./lib/service` passed. Tests cover mocked SSO, Run errors/options, and auth/proxy :0 address propagation. `git diff --check` passed.
