Updated the IA importer to separate publisher names and places, and to put ISBN-10 and ISBN-13 values in their respective Open Library fields. Added public parsing utilities and tests for string, list, mixed, whitespace, and empty inputs.

Verification: 29 focused tests and all 17 import API tests passed; `git diff --check` passed.