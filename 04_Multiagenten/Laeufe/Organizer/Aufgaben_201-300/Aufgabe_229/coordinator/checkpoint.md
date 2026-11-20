# Checkpoint

Task: clean up local group and user cover/avatar files on explicit removal and account deletion.
Status: implementation complete. Group cover and thumbnail cleanup uses validated local upload URLs; user image layer centralizes removal, local path lookup, and account deletion scanning of legacy and timestamped files. Socket handlers delegate to it and retain action hooks.
Validation: eslint passed on changed source and tests; mocha test/user.js test/groups.js passed (337 passing). No delegation used.
