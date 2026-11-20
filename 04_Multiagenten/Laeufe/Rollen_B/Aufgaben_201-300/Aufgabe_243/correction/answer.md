Fixed kube_service dialing so a failed selected endpoint is followed by attempts to the other discovered endpoints. The session records the address and server ID of the endpoint that succeeds. Added a regression test with one failed service and one healthy service.

Both reviewer flagged test commands pass, as does `git diff --check`. No remaining failures or test environment problems.