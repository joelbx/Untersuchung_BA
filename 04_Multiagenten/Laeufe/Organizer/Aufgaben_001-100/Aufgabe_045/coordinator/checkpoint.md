Task: Reject Python keywords in either segment of collection names.
Status: Implemented and verified.
Changes: AnsibleCollectionRef validates two Python identifiers and excludes keywords; Galaxy requirement classification reuses this validator; removed legacy dataclasses helpers and Python 2/3 fallback; added regression tests.
Verification: collection loader suite 70 passed; Galaxy collection and install suites 77 passed when run separately. A combined run is order dependent because the collection loader tests uninstall the finder needed by later Galaxy CLI tests.
Delegation: none.
