Updated the certificate error wrappers. WebKit now accepts `reply` and `errors`, renders single errors as paragraphs and multiple errors as lists, and escapes all message content. The shared decision methods and Qt 5/Qt 6 WebEngine wrappers are wired into their callers.

**Verification:** 54 related tests passed. Qt 6 was unavailable locally, so its wrapper was tested with a fake error object.