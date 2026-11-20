Updated Windows SSH stderr handling to replace complete embedded CLIXML blocks with readable UTF-8 bytes while preserving surrounding text and malformed or incomplete blocks. The PowerShell escape regex now matches UTF-16-BE hex digits precisely.

Added focused tests; all 49 relevant tests pass.