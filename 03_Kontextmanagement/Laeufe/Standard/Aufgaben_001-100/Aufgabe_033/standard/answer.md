U2F sign requests now include challenges for every registered key while retaining the original single-challenge JSON fields. The CLI uses the full list and still accepts responses from older servers. The web login test now registers two keys and verifies login with the second.

The focused web U2F login and auth MFA tests passed; the client package compiled.