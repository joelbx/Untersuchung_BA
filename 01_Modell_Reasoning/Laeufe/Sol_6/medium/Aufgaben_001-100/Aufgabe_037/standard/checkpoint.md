Issue: YAML dumping an AnsibleUndefined currently raises a PyYAML RepresenterError.
Plan: register an undefined representer, wrap YAML filter failures with filter context while retaining the original cause, and run relevant existing tests.
Status: complete. AnsibleUndefined now triggers Jinja's undefined error during YAML dumping. YAML filters wrap failures with their names and retain the original exception. Templar converts wrapped undefined causes to AnsibleUndefinedVariable. Relevant unit tests: 64 passed.
