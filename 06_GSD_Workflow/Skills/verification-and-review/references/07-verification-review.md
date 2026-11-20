# Phase 7: Verifikation und strukturiertes Review

**Eingang:** Implementierter Ticketumfang, freigegebene Kriterien und Prüfstrategie.
**Ausgang:** Belegtes Review des aktuellen Änderungsstands, bereit zur Abnahme.

Setze `reviewing`. Nutze `assets/review.md`. Erfasse den tatsächlichen Diff und
unversionierte relevante Dateien gegenüber dem Plan-Ausgangspunkt. Bei mehreren
Repositories jeden Stand getrennt behandeln; fremde Vorarbeiten nicht als eigene
Änderungen ausgeben. Keine Commits allein für einen Review-Fixpunkt erzwingen.

## Automatisierte und visuelle Prüfung

- Ordne jedem Akzeptanzkriterium Belege oder eine explizite Prüflücke zu.
- Führe vereinbarte Tests, Build und relevante Regressionen aus. Halte exakte
  Befehle, Arbeitsverzeichnis, geprüfte Codeversion, Exitcode und Ergebnis fest.
  Ein Wrapper kann trotz fehlgeschlagener Untertests Exitcode 0 liefern.
- Prüfe vereinbarte Fehlerfälle und Projekt-/Architekturkonventionen. Verwende
  bestehende statische Werkzeuge, statt deren Meldungen bloß als Review zu wiederholen.
- Bei Frontend: tatsächliche UI im vereinbarten Viewport/Zustand anzeigen und mit
  den benannten Mockup-Versionen vergleichen. Screenshots, nachvollziehbare
  Bildbezüge und Abweichungen sichern. Ohne Browser-/Bildprüfung visuelle Übereinstimmung
  als ungeprüft kennzeichnen, nicht aus CSS oder einer Build-Meldung ableiten.

## Zwei Review-Achsen

1. **Spec/Verhalten:** Kriterien erfüllt? Fehlende oder falsche Regeln, Randfälle,
   Mockup-Abweichungen, zusätzliche unvereinbarte Funktionalität?
2. **Standards/Struktur:** Bestehende Projektregeln und Schnittstellen eingehalten?
   Konkrete Wartbarkeits-, Fehlerbehandlungs- oder Integrationsprobleme?

Je Befund: Kennung, Schwere, konkrete Stelle/Beleg, Anforderungsbezug, Auswirkung,
Korrektur und erneuter Prüfschritt. Stilheuristiken als Einschätzung kennzeichnen;
belegte Projektregeln haben Vorrang. Befunde nicht zu einem pauschalen Qualitätswert
verrechnen, der ein Problem der einen Achse durch die andere verdeckt.

Die Phase beginnt mit neuem Agenten ohne Implementierungs-Chatverlauf. Sichere
Agent-/Phasenbezug und tatsächlich geprüften Code. Korrigiert der Reviewer selbst,
sind diese Korrekturen mit anschließender eigener Prüfung als **Selbstreview** zu
kennzeichnen. Ein neuer Prompt allein ist keine unabhängige Prüfung.

Korrigiere behebbare Befunde im gültigen Planumfang. Halte vorherige Befunde fest,
zähle Schleifen, und prüfe die betroffenen Stellen nach Änderungen erneut.
Wesentliche Scope-/Planänderungen führen zu erneuter Freigabe. Nicht behebbares oder
ungeprüftes Verhalten sichtbar lassen.

Bei vorhandener temporärer Prüfhilfe zunächst die menschliche Funktionsprüfung
vorbereiten; bis Rückbau und Abschlussverifikation bei `reviewing` bleiben.
Erst einen konsistenten, aktuell geprüften endgültigen Stand auf `acceptance` setzen und für
Phase 8 an die zentrale Steuerung zurückgeben. Wesentliche offene Korrekturen
bleiben `reviewing` oder blockiert. Ein grünes Review allein setzt niemals `done`.
