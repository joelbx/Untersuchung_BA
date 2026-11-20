Implemented chat allow and deny lists, a disable incoming messages setting, server-side checks for chat initiation and room creation, account controls, and an idempotent [upgrade](/app/src/upgrades/4.3.0/chat_allow_list.js) that migrates existing follow lists.

Verification: 356 messaging and user tests passed; lint and diff checks passed. Custom themes may need their own account controls.