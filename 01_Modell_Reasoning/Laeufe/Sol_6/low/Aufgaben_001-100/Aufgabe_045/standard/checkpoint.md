Task: fix FQCN keyword validation.
Status: completed.
Changes: centralized Python identifier and keyword validation in AnsibleCollectionRef; removed legacy dataclasses helpers; added regression cases.
Tests: collection loader 68 passed; collection install 30 passed when run separately. Combined run has shared collection-finder setup interference.
