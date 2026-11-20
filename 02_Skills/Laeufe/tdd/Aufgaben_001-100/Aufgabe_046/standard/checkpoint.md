# Checkpoint

Task: Repair collection module_utils dependency resolution in module_common.
Workflow: assigned test-driven-development; regression tests before production edits.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find.

## Implemented

- Queue-based module_utils dependency traversal with separate legacy and collection locators.
- Collection and legacy metadata redirect shims, FQCN expansion, target bundling, tombstones, and deprecations.
- Relative imports in package initializers, source-preserving package ancestors, synthesized missing initializers, base packages, six normalization, and candidate-path errors.
- Regression tests in `test/units/executor/module_common/test_collection_resolution.py`; adjusted pre-existing payload expectations for mandatory base package files.

## Verification

- `PYTHONPATH=lib python -m pytest -q test/units/executor/module_common/test_collection_resolution.py`: 8 passed.
- `PYTHONPATH=lib python -m pytest -q test/units/executor`: 85 passed.
- `git diff --check`: passed.
- `PYTHONPATH=lib python -m pytest -q`: interrupted after 12.12s due unrelated global collection/integration setup failures and CLI failures. At interruption: 25 failed, 39 passed, 19 errors, 79 rerun. This is not a passing full-suite check. Collection errors included `test/ansible_test/unit/test_diff.py` (missing ansible_test._internal), `test/ansible_test/validate-modules-unit/test_validate_modules_regex.py` (missing validate_modules), `test/integration/targets/async/library/async_test.py` and `async_fail/library/async_test.py` (module JSON input absent), `test/integration/targets/cli/test_k_and_K.py` (localhost SSH refused), `test/integration/targets/expect/files/test_command.py` (stdin captured), and integration collection modules imported without package context. Failures included `test/units/ansible_test/ci/test_azp.py::test_auth`, `test_shippable.py::test_auth`, `test/units/cli/test_adhoc.py` (KeyError args/module_name), and `test/units/cli/test_cli.py` (ansible.cli missing on patch target). These files are outside module_common.
- Added package redirect child regression after the first executor run. It failed because the alias package initializer was absent. Updated collection locator to generate package redirect shims and include child targets. Final `PYTHONPATH=lib python -m pytest -q test/units/executor`: 86 passed.
- Final `git diff --check`: passed.

## Bare pytest failures by name

The interrupted bare run displayed these failing test names:
`test/units/ansible_test/ci/test_azp.py::test_auth`,
`test/units/ansible_test/ci/test_shippable.py::test_auth`,
`test/units/cli/test_adhoc.py::{test_with_command,test_simple_command,test_no_argument,test_did_you_mean_playbook,test_play_ds_positive,test_play_ds_with_include_role,test_run_import_playbook}`,
`test/units/cli/test_cli.py::TestCliBuildVaultIds::{test,test_create_new_password_auto_prompt,test_create_new_password_no_vault_id,test_create_new_password_no_vault_id_ask_vault_pass,test_create_new_password_no_vault_id_no_auto_prompt,test_create_new_password_no_vault_ids_password_files,test_create_new_password_with_vault_ids,test_everything,test_no_vault_id_no_auto_prompt,test_no_vault_ids_auto_prompt,test_no_vault_ids_auto_prompt_ask_vault_pass}`,
`test/units/cli/test_cli.py::TestCliSetupVaultSecrets::{test,test_default_file_vault,test_default_file_vault_identity_list,test_multiple_prompts,test_multiple_prompts_and_ask_vault_pass}`.

Collection errors displayed:
`test/ansible_test/unit/test_diff.py`,
`test/ansible_test/validate-modules-unit/test_validate_modules_regex.py`,
`test/integration/targets/ansible-test/ansible_collections/ns/col/tests/unit/plugins/module_utils/test_my_util.py`,
`test/integration/targets/ansible-test/ansible_collections/ns/col/tests/unit/plugins/modules/test_hello.py`,
`test/integration/targets/ansible-test-docker/ansible_collections/ns/col/tests/unit/plugins/module_utils/test_my_util.py`,
`test/integration/targets/ansible-test-docker/ansible_collections/ns/col/tests/unit/plugins/modules/test_hello.py`,
`test/integration/targets/async/library/async_test.py`,
`test/integration/targets/async_fail/library/async_test.py`,
`test/integration/targets/cli/test_k_and_K.py`,
`test/integration/targets/expect/files/test_command.py`,
`test/integration/targets/module_utils/library/test_alias_deprecation.py`,
`test/integration/targets/module_utils/library/test_datetime.py`,
`test/integration/targets/module_utils/library/test_env_override.py`,
`test/integration/targets/module_utils/library/test_failure.py`,
`test/integration/targets/module_utils/library/test_override.py`,
`test/integration/targets/plugin_namespace/filter_plugins/test_filter.py`,
`test/integration/targets/plugin_namespace/test_plugins/test_test.py`,
`test/integration/targets/throttle/test_throttle.py`,
`test/integration/targets/collections_plugin_namespace/collection_root/ansible_collections/my_ns/my_col/plugins/test/test_test.py::test_name_ok`.
