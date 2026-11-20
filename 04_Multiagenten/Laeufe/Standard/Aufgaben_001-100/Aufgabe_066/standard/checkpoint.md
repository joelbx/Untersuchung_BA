Task: replace inline height values containing vh with auto in mail HTML preparation, after transformStylesheet and before transformRemote.
Status: complete. Added transformStyleAttributes, integrated it into prepareHtml, and added a focused unit test.
Verification: transformStyleAttributes and transformRemote Jest suites passed (5 tests total); git diff --check passed.
