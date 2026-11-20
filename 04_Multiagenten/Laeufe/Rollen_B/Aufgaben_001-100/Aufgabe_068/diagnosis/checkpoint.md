# Fault localization progress

- Located the entity REST client, wrapper, cache implementations, and existing tests. Source and tests remain untouched.
- `EntityRestClient.load` (line 114) and `loadMultiple` (line 173) do not accept a provided encrypted session key. Raw entities reach `resolveSessionKey` before decryption; `loadMultiple` goes through `_handleLoadMultipleResult` and `_decryptMapAndMigrate` (lines 237 and 251).
- `EntityClient` (lines 22 and 77) and `DefaultEntityRestCache` (lines 220, 237, 311) do not propagate optional key arguments. Cache misses call the underlying client with existing arguments only.
- Mail detail callers without key propagation: `MailUtils.loadMailDetails` (lines 397-407), `MailFacade.getReplyTos` (line 505), `MailIndexer.processNewMail` (lines 153-159), `MailIndexer.loadMailDetails` (lines 723-748, via `loadInChunks`), and `InboxRuleHandler.getMailDetails` (line 149).
- `CryptoFacade.resolveSessionKey` (line 192 onward) checks internal `sessionKeyCache` first, then the instance `_ownerEncSessionKey`; it decrypts that value with the owner group key when present. The explicit key should be placed on the raw entity before resolution. Blob and draft types are encrypted and include optional `_ownerEncSessionKey` in their models.
- Existing rest client tests cover single and batch requests, ownerKey behavior, and blob loading; cache tests cover forwarding and partial cache hits. No test execution or project edits performed.
