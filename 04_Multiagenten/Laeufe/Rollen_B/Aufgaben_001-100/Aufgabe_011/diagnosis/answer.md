I localized the issue but did not edit project source or tests: this run is restricted to fault diagnosis.

- [basic.py](/app/lib/ansible/module_utils/basic.py:344) uses `Ellipsis` for a missing `ANSIBLE_MODULE_ARGS`; [fail_json](/app/lib/ansible/module_utils/basic.py:1462) also uses it to distinguish an omitted exception from an active exception.
- [objects.py](/app/lib/ansible/parsing/yaml/objects.py:12) requires a positional value in all three legacy constructors, preventing the requested base-type construction patterns.
- [Templar](/app/lib/ansible/template/__init__.py:148) passes `None` overrides to [TemplateOverrides.merge](/app/lib/ansible/_internal/_templating/_jinja_bits.py:171), where validation rejects them.
- [Lookup handling](/app/lib/ansible/_internal/_templating/_jinja_plugins.py:262) omits the exception type for wrapped plugin errors and emits inconsistent warn and ignore messages.
- [Deprecation capture](/app/lib/ansible/utils/display.py:1152) stores module-result deprecations without a configuration check; the [module result path](/app/lib/ansible/executor/task_executor.py:832) forwards them. Direct `Display.deprecated` calls do check the setting and emit the disablement note, so the fix should cover both paths while preserving normal warnings.
- [timedout](/app/lib/ansible/plugins/test/core.py:48) returns the raw `period` value, which can be non-Boolean.
- The [CLI import-time error handler](/app/lib/ansible/cli/__init__.py:93) prints `str(ex)`, while [AnsibleError.__str__](/app/lib/ansible/errors/__init__.py:135) excludes help text. The reported “before display” failure most likely refers to this handler; that path should be checked against `cli_executor` before changing it.

The existing unit tests cover nearby behavior but do not establish the requested edge cases. I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).