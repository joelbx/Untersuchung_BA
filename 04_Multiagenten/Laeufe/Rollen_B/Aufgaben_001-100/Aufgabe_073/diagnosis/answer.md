I found two points where language metadata is lost:

- [`AmazonAPI.serialize()`](/app/openlibrary/core/vendors.py:184) reads `ItemInfo.ContentInfo` but never reads its `Languages` values. The import request already includes `ITEMINFO_CONTENTINFO`.
- [`clean_amazon_metadata_for_load()`](/app/openlibrary/core/vendors.py:473) omits `"languages"` from its accepted keys, so it would discard the field even after serialization adds it.

The fix should collect each `DisplayValue` from `Languages.DisplayValues`, exclude entries whose `Type` is `"Original Language"`, remove duplicates, preserve the supplied names and casing, and add the key only when values remain. The cleaner should then accept `"languages"`.

[Existing tests](/app/openlibrary/tests/core/test_vendors.py:245) contain language fixtures and a TODO, but do not assert this behavior. They also model `content_info` as a string, so the nested SDK shape remains unverified locally. **No project source or tests were edited**; this run was limited to fault localization.