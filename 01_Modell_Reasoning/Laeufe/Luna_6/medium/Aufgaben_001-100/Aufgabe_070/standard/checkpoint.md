# Checkpoint

Updated `format_languages` to build aliases from existing language records: ISO-639-1 codes, English names, and translated/native names map to MARC codes. Outputs are deduplicated in first-seen order.

Focused verification: `pytest -q openlibrary/tests/catalog/test_utils.py` collected 94 tests, with 90 passing and 4 formatter tests failing because `web.ctx.site` was absent from the test context. The pre-existing formatter also required `web.ctx.site`, so these failures appear to be test setup/context rather than an alias-resolution assertion. Review this limitation before considering the change complete.
