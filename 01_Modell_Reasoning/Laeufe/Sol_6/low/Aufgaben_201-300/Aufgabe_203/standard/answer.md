Added the reusable [ExternalLink component](/app/src/components/views/elements/ExternalLink.tsx) and its [SCSS partial](/app/res/css/views/elements/_ExternalLink.scss). The Profile Settings hosting signup now uses one named link with an external link icon and a screen reader cue. The Share dialog’s room link has a localized “Link to room” title.

`git diff --check` and localization JSON validation passed. Type checking reports existing `ThreadEvent` errors; the settings test could not start because the generated `component-index` is missing.

Other external links in the settings views have not yet been migrated to the new component, so the requested migration is incomplete.