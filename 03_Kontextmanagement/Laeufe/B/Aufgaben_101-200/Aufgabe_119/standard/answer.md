Refactored [Pill](/app/src/components/views/elements/Pill.tsx) into a functional component, added the public [usePermalink hook](/app/src/hooks/usePermalink.tsx), and updated callers to use named exports.

The pillify tests pass (3/3), and changed files pass ESLint and Prettier. Repository wide TypeScript checking still reports errors in unrelated SDK integration files.