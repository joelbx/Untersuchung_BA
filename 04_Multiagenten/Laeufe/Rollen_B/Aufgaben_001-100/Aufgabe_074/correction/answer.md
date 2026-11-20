Updated the subject indexing command in [Jenkinsfile](/app/scripts/solr_builder/Jenkinsfile:244) to use `--chunk_size`, `--solr_base_url`, and `--skip_id_check`, matching `FnToCLI`’s parameter names.

The reviewer’s exact test command passed: 13 tests. A direct parse of the Jenkins arguments also succeeded. No remaining failures or test environment problems.