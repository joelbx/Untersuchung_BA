Refactored Worksearch Solr handling to consume JSON, default `wt` to `json`, and process flat facet arrays through the new `process_facet` and `process_facet_counts` generators. Converted `get_doc` to use JSON documents and added `first_edition` to the default fields.

Updated the existing Worksearch tests for the JSON interfaces. All 25 focused tests passed, and `git diff --check` passed.