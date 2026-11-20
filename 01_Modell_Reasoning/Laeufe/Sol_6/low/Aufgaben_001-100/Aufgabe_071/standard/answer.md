Updated the PowerShell CLIXML parser to decode UTF-16 escape sequences, including surrogate pairs and control characters. It now filters `<S>` elements by stream, handles empty elements, joins text within each block directly, and adds CRLF only between blocks with matching text.

Updated the tests; all 7 PowerShell shell tests pass.