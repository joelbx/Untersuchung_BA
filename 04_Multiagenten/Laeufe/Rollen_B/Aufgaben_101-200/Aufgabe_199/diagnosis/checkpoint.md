# Fault localization checkpoint

Inspected `openlibrary/catalog/get_ia.py`, `openlibrary/tests/catalog/test_get_ia.py`, and the deprecated `openlibrary/catalog/marc/marc_subject.py` caller. No project source or tests changed.

- `get_ia.py:9,29-39` imports `six.moves.urllib`; `urlopen_keep_trying` accepts only a URL, returns a file handle, and uses urllib HTTP/URL errors. Requests conversion needs `requests.get(url, headers=headers, **kwargs)`, `raise_for_status()`, `HTTPError.response.status_code` checks for 403/404/416, and retry handling for other request failures.
- `get_ia.py:49,71-82,99-105,157-162,204-205,224-226` consumes `.read()` or passes file handles to lxml. Binary MARC and raw XML should use response `.content`; text use `.text` with UTF-8 fallback when no charset. `etree.fromstring(response.content)` handles byte XML; `etree.parse` cannot accept raw response bytes as a file stream.
- `get_ia.py:157-161` builds a urllib Request for Range and reads at most `MAX_MARC_LENGTH`; preserve the cap with `.content[:MAX_MARC_LENGTH]` and pass the Range header to the helper.
- `get_ia.py:95-107` makes an unconditional second request even after a successful XML parse, and catches expat errors rather than lxml XMLSyntaxError. This may affect retries during migration.
- Existing `test_get_ia.py:9-21,75-99` monkeypatches `urlopen_keep_trying` with binary file handles. These fixtures do not model a requests Response and will fail if consumers switch to `.content`. No existing tests found for retry statuses, Range headers, encoding, or XML file listings.
- Deprecated `marc_subject.py:56-70` imports the helper and still calls `.read()` / passes the response to `etree.parse`; changing the helper return type will break those callers unless addressed separately.
