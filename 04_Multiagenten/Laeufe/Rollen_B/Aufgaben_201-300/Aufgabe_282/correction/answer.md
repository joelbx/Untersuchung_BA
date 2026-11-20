Removed the unsupported `debug` value from [content.javascript.log_message.levels](/app/qutebrowser/config/configdata.yml:946). JavaScript sources provide `info`, `warning`, and `error` levels; `debug` is a standard logger destination.

The reviewer’s exact test command passed: **1,151 passed, 10 xfailed**. No remaining failures.