# Persistenz, Status und Freigaben

## Artefaktstruktur im Projekt

Nutze vorhandene Dokumentationsregeln; die folgende Struktur ist ein überschreibbarer
Standard innerhalb eines Feature-Artefaktordners, kein Framework-Pfad:

```text
workflow.json
specifications/S1.md
decisions.md
approvals.jsonl
events.jsonl
tickets/T-001-T1.md
plans/T-001-P1.md
reviews/T-001-R1.md
acceptance/T-001-A1.md
metrics/T-001.json
evidence/                 nur tatsächlich erzeugte Logs/Bilder/Prüfbelege
```

Erzeuge Dateien bedarfsweise. Ordne Eingabeanforderungen und Mockups als Quellen zu;
kopiere/veröffentliche keine vertraulichen Dokumente ohne Aufgabenbezug. Referenziere
vorhandene Bilder mit Pfad oder stabiler URL, Version/Hash, relevantem Ausschnitt und
vereinbartem Viewport. Ein geänderter Dateiname ersetzt keine Bildprüfung.

`workflow.json` ist der kompakte Einstieg: Feature-ID, Repository-Bezüge,
Artefaktpfade, Status, aktuelles/nächstes Ticket, Blocker und Freigabe-IDs.
Tickets enthalten mindestens `id`, `status`, `spec_revision`, `plan_revision`,
`spec_approval`, `plan_approval`, `acceptance_approval` und `artifacts`.
Pfadwerte in `artifacts` beziehen sich auf diesen Artefaktordner.
Nutze die unveränderte Struktur aus der Workflow-Vorlage; füge Tickets erst hinzu,
wenn ihre ID bekannt ist. Leere Vorlagen sind keine ausgefüllten Nachweise.

## Zwei Status-Ebenen

Feature: `draft → clarification → specified → approved → planned → implementing
→ reviewing → acceptance → done`.

Ticket: `draft → planned → implementing → reviewing → acceptance → done`.

`planned` bedeutet **Plan liegt vor**, nicht **Plan ist freigegeben**.
Ein Feature kann `implementing` bleiben, während einzelne Tickets bereits `done`
sind. Es ist erst `done`, wenn alle Tickets ausdrücklich abgenommen, Blocker
geschlossen und die Dokumentation vervollständigt sind. Eine weitere pauschale
Feature-Abnahme ist kein zusätzliches Pflicht-Gate.

Blocker stehen separat mit Grund, betroffenem Schritt und benötigter Entscheidung;
ein Messwert `unavailable` blockiert allein keine Entwicklung.

## Gate-Belege

Nach einer tatsächlichen Nutzerentscheidung einen Beleg nach der Freigabevorlage
an `approvals.jsonl` anhängen. Er muss enthalten:

- eindeutige ID, Art (`specification`, `implementation_plan`, `acceptance`),
  Feature-/Ticketbezug und vorgelegte Revision;
- `actor: human`, echte Aussage des Nutzers, Herkunft des Belegs sowie Zeit, falls
  zuverlässig bekannt; eine nicht verfügbare Message-ID bleibt `null`;
- `artifacts`: relative Pfade und tatsächlich berechnete SHA256-Werte der
  freigegebenen Artefakte, keine erfundenen Fingerprints.

Ein kurzes „ja“ genügt nur, wenn es eindeutig genau der unmittelbar gestellten,
konkret verlinkten Freigabeanfrage zugeordnet werden kann. Bei mehreren möglichen
Bezügen klären. Bestehende ausdrückliche Autorisierung verwenden, wenn ihr Umfang
die konkrete vorgelegte Version abdeckt; nicht einfach erneut fragen.

Spec-Beleg umfasst die Spezifikation und fachlich relevante externe Mockup-/Quellen-
Versionen über deren in der Spezifikation festgehaltene Identität. Plan-Beleg
umfasst **Ticket und Plan**; diese verweisen auf die freigegebene Spec-Revision.
Abnahme-Beleg umfasst Review und Abnahmedokument; darin die bewertete Codebasis
festhalten (Commit oder Diff-Hash **einschließlich unversionierter Änderungen**,
bei mehreren Repositories getrennt). Niemals Freigabetext nachträglich ergänzen.
Die Freigabe-IDs im Status speichern, ohne die gehashten Artefakte danach nur zur
Eintragung der Freigabe wieder zu ändern.

Bei Scope-, Akzeptanzkriterien-, Schnittstellen- oder wesentlichen Planänderungen
neue Revision erstellen, betroffene Freigabe als abgelöst dokumentieren und erneut
vorlegen. Nicht betroffene Tickets behalten ihre gültigen Belege. Bei reiner
Korrektur innerhalb des gültigen Plans keine neue Planfreigabe erzwingen.
Eine neue Codeänderung nach Abnahme benötigt erneutes Review/Abnahme oder ein neues
Ticket; die alte Abnahme bleibt als historische Entscheidung erhalten.

Verwende für freizugebende Artefakte von Anfang an versionierte Dateipfade. Bereits
freigegebene Dateien nicht überschreiben; neue Revision in neuer Datei ablegen und
den aktuellen Pfad im Zustand umstellen. Ticketstatus gehört in `workflow.json`,
nicht als nachträgliche Änderung in ein freigegebenes Ticketdokument. So können
unbetroffene Tickets weiterhin auf ihre ältere, gültige Spec-Version verweisen.
Jedes Ticket hat dafür einen eigenen `artifacts.specification`-Pfad und Spec-Beleg.

## Wiederaufnahme und Konsistenz

1. Zustand, betroffene Artefakte, offene Fragen und Belegdatei lesen.
2. Prüfen, ob Freigabeart, Gegenstand, Revision und tatsächliche Artefakthashes passen.
   Änderung der Codebasis/Mockup-Quelle seit dem Review ebenfalls prüfen.
3. Fehlende, widersprüchliche oder veraltete Belege als Blocker zeigen. Nicht aus
   einem Summary oder dem bloßen Statuswort `approved` rekonstruieren.
4. Letzten sicheren Zustand benennen; nur den davon erlaubten Schritt fortführen.
   Abgebrochene Tests gelten nicht als bestanden und müssen bei Bedarf erneut laufen.
5. Nach jedem Übergang Zustand und Ereignisjournal aktualisieren; vor Pause zusätzlich
   letzten Stand, nächste Aktion und nötige Freigabe sichern. Bestehende Einträge
   nicht umschreiben, Korrekturen als neue Ereignisse hinzufügen.

Optional `python3 <skill-root>/scripts/check_workflow.py <artefaktordner>` ausführen.
Der Prüfer schreibt nichts und prüft nur dokumentierte Struktur/Hashes/Gates.
Er authentifiziert keinen Menschen, analysiert keinen Code und ersetzt weder
semantische Freigabeprüfung noch Abnahme. Anweisungen und JSON sind keine technische
Sicherheitsgrenze gegen einen Agenten, der sie missachtet.

## Phasenagenten ab Bundle 1.3.0

`execution.mode: sequential_fresh_phase_agents`, `execution.phase` und
`phase_agent_attempts` beschreiben die Ausführung. Pro Versuch: `attempt_id`, Phase,
Ticket oder `null`, tatsächliche `agent_id`/`thread_id`, `context_mode`,
`context_mode_evidence`, `handoff_path`, `handoff_sha256`, Beginn/Ende, Status und
Vorgängerversuch. Ein laufender Worker bleibt auf dieselbe Phase begrenzt.
Übergaben unter `handoffs/<scope>-<phase>-<attempt>.json` aus der
[Vorlage](../assets/phase-agent-handoff.json) finalisieren; erforderliche Artefakte
als `path`, `sha256`, `purpose` angeben. Pfade relativ zum Feature-Ordner, Projekt-
und Feature-Wurzeln absolut. Die Übergabe danach nicht umschreiben. Laufzeit-IDs
und tatsächliche Zeiten im Zustand erfassen; Vorlagenwerte sind keine Messdaten.

Alte `ticket_agent_attempts` nur als Historie behalten, nicht zu getrennten Phasen
umetikettieren. Fehlende Felder belegen keine frischen Kontexte. Versionswechsel
mit der tatsächlich nächsten Phase und unveränderten Freigaben dokumentieren.

Neue Tickets erhalten `temporary_test_aids: []` oder inventarisierte Prüfhilfen.
Die [Rückbauregel](temporary-test-aids.md) bestimmt zusätzliche Voraussetzungen für
`done`. Alte Tickets ohne dieses Feld bleiben lesbar; das beweist keinen geprüften
Rückbau. Vor Fortführung alter offener Tickets den tatsächlichen Hilfenbestand prüfen.
