Task: Add Amazon edition languages to serialized metadata and preserve them for load.
Status: Complete. Serializer reads ContentInfo.Languages.DisplayValues, excludes Original Language, deduplicates names, and omits empty languages. Loader allowlist preserves languages. Relevant vendor tests pass (36).
