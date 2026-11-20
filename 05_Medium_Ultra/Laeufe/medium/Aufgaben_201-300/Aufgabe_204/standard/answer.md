Updated contact import to parse ISO dates, English month-name dates, and the requested slash formats. Unparseable dates remain unset, and the new tests confirm that parsed calendar dates serialize correctly to vCard.

TypeScript, formatting, and diff checks pass. The shared test suite had **877 passes and 2 unrelated failures** in base64 and cookie helpers.