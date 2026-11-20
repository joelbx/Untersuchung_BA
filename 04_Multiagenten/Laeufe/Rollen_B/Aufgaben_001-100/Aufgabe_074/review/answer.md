VERDICT: FIX

**Code defect:** [FnToCLI](/app/scripts/solr_builder/solr_builder/fn_to_cli.py:81) now generates underscore option names, but the subject-indexing command in [Jenkinsfile](/app/scripts/solr_builder/Jenkinsfile:244) still passes `--chunk-size`, `--solr-base-url`, and `--skip-id-check`. A local reproduction exits with code 2 and reports those arguments as unrecognized. Update that command to `--chunk_size`, `--solr_base_url`, and `--skip_id_check`.

**Tests:** `python -m pytest scripts/solr_builder/tests/test_fn_to_cli.py -q` — 13 passed. `TEST_ENVIRONMENT_PROBLEM`: none. No project code was changed during this review.