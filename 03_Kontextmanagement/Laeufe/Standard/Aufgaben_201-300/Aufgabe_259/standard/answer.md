Updated the Solr work builder to select a public IA edition for `lending_edition_s` when one exists and pair it with the correct IA identifier. It also treats lending-library editions as borrowable. The work document retains the IA IDs, combined collections, and print-disabled edition IDs.

Added a multi-edition regression test. All 60 Solr tests pass.