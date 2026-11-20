Fixed the YAML undefined-variable error. `AnsibleDumper` now lets Jinja report the missing variable, and `to_yaml` and `to_nice_yaml` raise filter-specific `AnsibleFilterError` messages while preserving the underlying exception.

The relevant unit tests passed: **50 passed**. The broader YAML test run had one unrelated setup error because the local pytest installation lacks the `mocker` fixture.