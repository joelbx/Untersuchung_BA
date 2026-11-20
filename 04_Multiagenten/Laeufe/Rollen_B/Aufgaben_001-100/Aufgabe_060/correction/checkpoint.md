Correction round started: inspecting reviewer findings and current patch.
Implemented identifier-only book import and compatible remote-ID candidate selection; added regression tests. Initial test run exposed a models/load_book import cycle, fixed with a local import.
Final verification: reviewer test commands passed (125 add-book tests; 40 core/merge-author tests); git diff --check clean. No remaining failures.
