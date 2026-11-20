Updated the controller minimum to Python 3.12, removed older controller compatibility fallbacks, and changed collection directory extraction to pass the original name to `TarFile.getmember()`. Missing members now raise the requested `AnsibleError`; the extraction tests verify the lookup and message.

Added a breaking change entry in [python-3.12-controller.yml](/app/changelogs/fragments/python-3.12-controller.yml).

Verification: focused extraction tests passed (3); `git diff --check` passed. The tests ran under Python 3.11, so they did not exercise the new controller version guard.