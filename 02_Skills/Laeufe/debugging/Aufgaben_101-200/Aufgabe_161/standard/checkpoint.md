# Worksearch Solr JSON migration checkpoint

Status: investigating current code and tests.

`rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep` for local inspection.

Root cause: `run_solr_query` omitted `wt` by default, and the search page parsed `response`, facets, spellcheck, and docs through lxml. Solr JSON uses `response.docs` dictionaries and flat alternating facet lists. Nearby `works_by_author` and `work_search` already use JSON.

Hypothesis: requesting JSON by default and consuming these JSON shapes directly resolves the page mismatch. A regression test was executed before implementation: `python -m pytest openlibrary/plugins/worksearch/tests/test_worksearch.py -q -x` failed during collection because `process_facet` did not exist, as expected.

Implementation: `run_solr_query` now always sends `wt`, defaulting to `json`; `do_search` consumes JSON response, facets and spellcheck; `get_doc` reads JSON document keys. XML facet parsing was replaced with `process_facet` and `process_facet_counts`. The search template displays string errors from JSON parsing.

Verification: `python -m pytest openlibrary/plugins/worksearch/tests -q` passed (28 tests); `git diff --check` passed. Earlier test failure (`NameError: solr_select_url`) came from missing plugin config in the isolated query test; the test now supplies that URL through monkeypatch. No external tooling was used.
