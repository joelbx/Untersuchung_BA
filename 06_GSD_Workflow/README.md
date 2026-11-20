# Guided Software Development (GSD)

Dieser Ordner ergänzt die fünf Benchmark-Versuchsreihen um den daraus abgeleiteten
Workflow-Skill. Er ist keine weitere 300-Aufgaben-Benchmarkreihe.

Kopiert wurde der **aktuell installierte Stand** aus `~/.agents/skills`, einschließlich
der dort vorhandenen Änderungen. Die Inhalte wurden nicht auf eine ältere Fassung
zurückgesetzt oder redaktionell verändert. Versionen, Dateigrößen, ursprüngliche
Pfade und SHA-256 stehen in [Herkunft.json](Herkunft.json).

## Bestandteile

| Skill | Aufgabe |
|---|---|
| [guided-software-development](Skills/guided-software-development/SKILL.md) | Übergeordnete Steuerung, Freigaben und Phasenübergänge |
| [requirements-clarification](Skills/requirements-clarification/SKILL.md) | Anforderungen und Ticketfragen klären |
| [specification-and-ticketing](Skills/specification-and-ticketing/SKILL.md) | Spezifikation und Tickets erstellen |
| [ticket-planning](Skills/ticket-planning/SKILL.md) | Implementierungsplan erstellen |
| [ticket-implementation](Skills/ticket-implementation/SKILL.md) | Freigegebenes Ticket implementieren |
| [verification-and-review](Skills/verification-and-review/SKILL.md) | Verifizieren, reviewen und Nachbesserungen prüfen |

Die sechs Ordner liegen als Geschwister unter `Skills/`, damit ihre relativen
Querverweise funktionieren. Alle Referenzen, Vorlagen, Quellen-/Anpassungsnachweise,
Agentenmetadaten, der Zustandsprüfer und die vorhandenen lokalen Tests sind enthalten.

[Ausführliche Verwendung und Installation](Skills/guided-software-development/README.md)

Für eine Installation müssen alle sechs Skillordner gemeinsam in ein geeignetes
Skillverzeichnis kopiert werden. Diese Archivkopie installiert oder aktiviert sie
nicht automatisch und startet keinen Entwicklungsworkflow.

Die lokalen Tests prüfen die gespeicherten Freigabe- und Zustandsregeln anhand
künstlicher Artefakte. Sie belegen nicht die Wirksamkeit des Workflows in einem
realen Softwareprojekt. Ihre tatsächliche Ausgabe steht in `Pruefung.txt`.
