# Quellen, Bestandsaufnahme und Anpassungen

Prüfstand: 2026-10-29. Die unten genannten Originaldateien wurden tatsächlich
gelesen; Namen allein waren keine Funktionsbeschreibung. Eigene Anweisungen wurden
für den gewünschten Ablauf formuliert, Original-Skills nicht vollständig gebündelt.
Der Skill funktioniert ohne Installation der beschriebenen Fremd-Skills.

## Formate und Codex

- [Agent Skills Specification](https://agentskills.io/specification): Ordnername,
  YAML-Frontmatter mit `name`/`description`, Ressourcenordner und Progressive
  Disclosure. Hauptdatei bewusst kurz; Referenzen direkt von dort erreichbar.
- [Codex: Build skills](https://learn.chatgpt.com/docs/build-skills): benutzerweite
  Discovery unter `~/.agents/skills`, explizite Aktivierung über `$`, optionale
  UI-Metadaten und Neustart bei fehlender Erkennung. Keine Änderung an config.toml.

## Tatsächlich untersuchte Matt-Pocock-Skills

Repository: [mattpocock/skills](https://github.com/mattpocock/skills), geprüft am Commit
`59db609eb1e18aaf59b63284d0e52255aff0c63c`. Einzelpfade und SHA256 stehen in sources.json.

| Quelle | Tatsächlicher Inhalt / Voraussetzung | Übernahme und bewusste Anpassung |
|---|---|---|
| `grill-me` | Kleiner Wrapper, ruft `grilling` auf; hostabhängiges Invocation-Frontmatter. | Keine Namensmagie vorausgesetzt; eigener Klärungsablauf. |
| `grilling` | Entscheidungsbaum, aktuell beantwortbare Fragen, Empfehlungen und Abschluss bei gemeinsamem Verständnis; delegiert Faktenrecherche an Unteragenten. | Entscheidungsabhängigkeiten und Faktenrecherche übernommen; standardmäßig eine Frage nach der anderen, kein verpflichtender Unteragent. |
| `grill-with-docs` | Wrapper, ruft `grilling` und `domain-modeling` auf. | Eigenständige Klärung plus dauerhafte Entscheidungen; kein Tool-Aufruf einer nicht installierten Abhängigkeit. |
| `domain-modeling` | Glossar, konkrete Szenarien, Codeabgleich; ADRs nur bei dauerhaften, begründeten Entscheidungen. | Vorhandene Fachsprache/ADRs berücksichtigen; keine neuen globalen Glossar-/ADR-Dateien ohne Bedarf. |
| `to-spec` | Synthese vorhandener Klärung, Prüfgrenzen abstimmen; setzt Tracker-/Labelkonfiguration voraus und veröffentlicht die Spec. | Dauerhafte lokale Spec mit Quellen, Mockups und Kriterien; Anforderungen von Vorschlägen getrennt; ausdrückliche menschliche Freigabe statt automatischer Veröffentlichungsreife. |
| `to-tickets` | Vertikale Schnitte, Blocking-Kanten, Feedback zum Zuschnitt; lokale Dateien oder konfigurierter Tracker. | Rückverfolgbare kleine Tickets und Abhängigkeiten; lokaler Standard, keine automatischen Issues; Ticketplan-Freigabe statt zusätzlichem pauschalen Pflicht-Gate. |
| `tdd` | Verhalten an vorab vereinbarten öffentlichen Prüfgrenzen; kleine Red-Green-Schnitte; verweist auf Test-/Mocking-Referenzen und ggf. `codebase-design`; verschiebt Refactoring ins Review. | Prüfgrenzen im Plan freigeben, Verhaltenstests und echte Red-Nachweise; Refactoring bei grünen Tests innerhalb des genehmigten Umfangs ausdrücklich erlaubt, visuelle Alternativen dokumentieren. |
| `code-review` | Standards-/Spec-Achsen; benötigt Tracker-/Spec-Kontext und einen Git-Fixpunkt; fordert zwei parallele Unteragenten und betrachtet den Commit-Diff. | Zwei Achsen übernommen; Selbstreview möglich und so benannt; tatsächlichen Arbeitsdiff samt unversionierten Dateien erfassen; kein verpflichtender Tracker, Commit oder zweiter paralleler Reviewer; siehe aktuellen Phasenvertrag unten. |
| `setup-matt-pocock-skills` | Bestätigte Tracker-/Label-/Domain-Dokumentkonfiguration; kann Projektdateien, Remotes und Labels verändern. | Keine automatische Ausführung; bestehende Konventionen lesen und lokal funktionsfähig bleiben. |

## Lokale Bestandsaufnahme

- Benutzerweit vorhanden: `grill-me` als Wrapper und `grilling` mit dem beschriebenen
  Entscheidungsbaum. Ihre tatsächlichen lokalen Texte wurden gelesen und gehasht.
- Die aktuellen, benutzerseitig verfügbaren System-Skills enthalten insbesondere
  `skill-creator`, `openai-docs` und `skill-installer`; sie sind Erstellungs-/Setup-
  Hilfen, keine versteckten Laufzeitabhängigkeiten dieses Workflows.
- Im untersuchten Projektbereich existieren außerdem `cucumber-migration`,
  `frontend-migration`, `gitlab-wiki-docs`, `glab`, `legacy-extraction` und
  `manage-liquibase-changesets`. Diese wurden als spezialisierte Projekt-Skills
  inventarisiert, für den generischen Ablauf aber nicht benötigt oder aufgerufen.
- In den geprüften Skillwurzeln waren `to-spec`, `to-tickets`, `tdd` und
  `code-review` nicht installiert. Die Quellversionen waren öffentlich erreichbar.
- Im Benchmarklabor liegen außerdem eingefrorene Superpowers-Versuchsdateien
  außerhalb dieser Skillwurzeln. Sie sind keine automatisch verfügbaren globalen
  Skills und werden hier weder verändert noch als Laufzeitabhängigkeit verwendet.
- Projektübersicht und geltende Einstiegsdateien zeigen mehrere Repositories und
  bestehende Konventionen. Deshalb wird weder ein Anwendungsprojekt vorausgewählt
  noch ein fremdes AGENTS.md/Repository geändert. Der Skill bleibt projektunabhängig.

## Eigenständige Ergänzungen

Die drei menschlichen Gates, Versions-/Hash-Belege, Trennung von Feature- und
Ticketstatus, explizite Abnahme vor done, Wiederaufnahmeprüfung und Messvorlagen
sind auf die Nutzeranforderungen zugeschnitten. Sie sind kein experimenteller
Wirksamkeitsnachweis. Die vorgeschlagene Zeit-/Token-Erfassung vermeidet erfundene
Werte und dokumentiert zusätzliche Agenten, Unterbrechungen und menschliche Eingriffe.

Keine externen Tracker- oder Kommunikationsaktionen wurden bei der Erstellung
ausgeführt. Keine Unteragenten wurden für ein vermeintlich unabhängiges Review
verwendet. Die Validierung umfasst Struktur und lokale Zustands-Fixtures; eine
erfolgreiche echte Projektanwendung wird nicht behauptet.

## Architekturänderung in Bundle 1.1.0

Auf ausdrücklichen Nutzerwunsch wurden Aufnahme/Klärung, Spec/Tickets, Ticketplanung,
Implementierung und Verifikation/Review in fünf eigene Skills ausgelagert. Ihre
fachlichen Referenzen und Vorlagen wurden verschoben, nicht vollständig dupliziert.
Der Oberskill behält gemeinsame Regeln, Persistenz, Freigaben, Abnahme und Messmodell.
Die Unter-Skills prüfen dieselben Voraussetzungen auch bei direktem Aufruf.

Das ist eigene Komposition, kein Original-Workflow von Matt Pocock. Die beiden
Spec-Modi bleiben durch die menschliche Spec-Freigabe getrennt; Planfreigabe und
Ticketabnahme wurden nicht abgeschwächt. In Version 1.1.0 war Einzelagent/Selbstreview der Standard; seit 1.3.0 gilt der unten dokumentierte Phasenvertrag.
Bundle-Routing allein erzeugt weder unabhängige Reviewer noch frische Kontexte.

## Bundle 1.2.0: explizite Ticket-Agenten

Auf Nutzerwunsch ergänzt: sequenzielle Ticketschleife, neuer Agent ohne geerbten
Gesprächsverlauf je Ticket, ticketbezogene Grill-me-Klärung vor der Planfreigabe.
Dies ist eine eigene Workflow-Anpassung, kein behauptetes Verhalten des originalen
Matt-Pocock-Skills. Dessen Fragerunden werden zu Einzelfragen; seine Recherche-
Subagenten werden durch eigene lesende Faktenprüfung ersetzt. Freigaben bleiben
verbindlich. Kein leerer Systemkontext und keine Dateisystemisolation behauptet.
Laufzeitbezug: [Codex-Subagenten](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[OpenAI Multi-Agent-Kontextübergabe](https://developers.openai.com/api/docs/guides/responses-multi-agent).
Bei der Skill-Erstellung wurden keine echten Feature-Ticket-Agenten gestartet.

## Bundle 1.3.0: gemeinsam geklärte Phasenkontexte

Der Nutzer hat nach Einzelklärung ausdrücklich festgelegt: frischer Kontext je
Phase einschließlich Feature-Phasen; Ticket-Grilling getrennt von Planung; TDD
in einem Implementierungskontext; Reviewer darf selbst korrigieren; nächstes
Ticket erst nach Endabnahme. Temporäre Prüfhilfe ist zulässig, mit menschlicher
Funktionsprüfung, verbindlichem Rückbau und frischer Abschlussverifikation vor
Endabnahme. Diese Entscheidungen ersetzen den Ticket-Agentenentwurf aus 1.2.0.
Die konkrete Phase wird als enger Auftrag delegiert, nicht der gesamte Koordinator.
Kontexttrennung und Prüfhilfenprotokoll sind eigene Workflow-Konzepte, keine
Behauptung über das Verhalten der unveränderten externen Skills.
