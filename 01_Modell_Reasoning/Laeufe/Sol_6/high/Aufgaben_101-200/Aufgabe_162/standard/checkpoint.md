Goal: Add optional encoding validation to FormatString during to_py conversion, matching String behavior.
Status: Complete. FormatString reuses String encoding validation; user agent requires ASCII. Configtypes/configdata tests: 1140 passed, 10 xfailed. Configfiles tests: 206 passed, 1 skipped. Websettings suite has an environment failure because PyQt5.QtWebKit is unavailable. git diff --check passes.
Constraints: Use local code and existing tests; preserve behavior when encoding is omitted.
