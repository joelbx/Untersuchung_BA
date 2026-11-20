Task: Add an idempotent NIOS fixed address module for IPv4 and IPv6.
Status: Complete. Added the IPv4/IPv6 fixed address module, scoped WAPI lookup and collection comparison, and unit coverage. All 74 NIOS unit tests pass; Python compilation, YAML parsing, and git diff whitespace checks pass. The validate-modules script cannot start because the local voluptuous dependency is absent.
