Added `content.javascript.log_message.excludes` so source and message glob patterns can suppress specific JavaScript messages from the UI. The existing source and level rules now live under `.levels`, with saved values migrated automatically. Excluded messages still follow the standard logger setting.

Updated the settings reference and added focused tests. **42 tests passed**.