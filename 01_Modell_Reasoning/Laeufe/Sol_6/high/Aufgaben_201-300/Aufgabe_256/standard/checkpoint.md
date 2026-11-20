Task: Fix Play hosts validation and dynamic name derivation for invalid hosts values.
Status: Complete. Play.load no longer derives or mutates name; get_name derives it dynamically; _validate_hosts reports parser errors for invalid present hosts values. Updated unit and integration assertions.
Verification: 249 playbook unit tests passed; CLI empty-host playbook reports the required parser error; git diff --check passed.
Constraints: Work only in checked-out files; no git history, index baseline, or harness changes.
