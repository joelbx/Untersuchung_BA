Task: Reject Python keywords in collection names.
Status: Complete. Shared validation rejects Python keywords in either segment, and Galaxy requirements and references use it. Updated the CLI fixture that treated `abc.def` as valid.
Verification: Collection loader (85), Galaxy requirements (40), Galaxy collection (48), CLI collection listing (6), and Galaxy CLI (110) tests passed in separate processes. The Galaxy CLI suite was run with ANSIBLE_DEVEL_WARNING=False because its warning-count assertions otherwise include the development warning. `git diff --check` passed.
