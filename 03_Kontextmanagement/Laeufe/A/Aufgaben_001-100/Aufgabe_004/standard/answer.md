Fixed the PassAliases drawer. It now shows the alias list when aliases are present, displays **“No aliases”** when empty, and opens the creation modal from **“Get an alias.”** The provider also handles users without a vault by creating one when they start the alias flow.

Verification passed: 6 existing tests, TypeScript checks for both affected packages, and Prettier.