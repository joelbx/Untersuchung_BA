Added `content.javascript.log_message.levels` and `content.javascript.log_message.excludes` in [configdata.yml](/app/qutebrowser/config/configdata.yml), with a migration alias for the old setting. The new `_js_log_to_ui` helper applies source, level, and message globs; excluded messages still reach the standard logger.

The focused browser and config tests passed: **43 passed**.