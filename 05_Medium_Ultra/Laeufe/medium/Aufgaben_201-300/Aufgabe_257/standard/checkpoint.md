# Checkpoint

Issue: tsh testability and runtime listener addresses.

Completed: tsh command handlers and Run return errors; Run accepts post-parse CLIConf options; SSOLoginFunc and MockSSOLogin propagate through makeClient and override ssoLogin; auth and proxy runtime listener addresses propagate into service configuration, proxy settings, dependent components, and logs. Added focused tsh tests.

Verification: package compilation passed; selected existing tsh, client, and service tests passed. Final selected test run in progress.
