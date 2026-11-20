Task: expose Project Runeberg identifiers in work search documents and add provider integration/templates.
Status: implemented in checked-out files. Work search fetches id_project_runeberg and returns the list or []; provider registered with acquisition URL and IA identifier detection; Runeberg read/download templates added.
Verification: 5 focused existing/new tests passed; both templates compiled; provider smoke check passed; git diff --check passed.
Note: Runeberg format-specific download endpoints were not documented locally, so format choices link to the edition page, where available files can be selected.
