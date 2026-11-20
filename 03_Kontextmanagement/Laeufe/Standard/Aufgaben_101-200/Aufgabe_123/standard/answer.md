Updated notifications to render string HTML through DOMPurify and give rendered links `target="_blank"` and `rel="noopener noreferrer"`. Non-success notifications now deduplicate by an explicit key, or by string text when no key is supplied; repeated success notifications can still appear.

Added focused tests. All 5 pass, and the components TypeScript check and targeted ESLint check pass.