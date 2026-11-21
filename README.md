# Untersuchung

Die Dateien wurden mit der Hilfe von Codex entsprechend der Versuche in separaten Ordnern organisiert.

Jede Versuchsreihe hat einen eigenen Ordner mit klar zugeordneten Runnern,
Auswertungsskripten, Konfigurationen, Endläufen und Ergebnissen.

| Versuchsreihe | Einstieg | Finaler Bericht |
|---|---|---|
| Modell und Reasoning | [01_Modell_Reasoning](01_Modell_Reasoning/README.md) | [Ergebnisse](01_Modell_Reasoning/Ergebnisse/reasoning-comparison.md) |
| Skills | [02_Skills](02_Skills/README.md) | [Ergebnisse](02_Skills/Ergebnisse/summary.md) |
| Kontextmanagement | [03_Kontextmanagement](03_Kontextmanagement/README.md) | [Ergebnisse](03_Kontextmanagement/Ergebnisse/report.md) |
| Feste Rollen und Organizer | [04_Multiagenten](04_Multiagenten/README.md) | [Ergebnisse](04_Multiagenten/Ergebnisse/summary.md) |
| Medium und natives Ultra | [05_Medium_Ultra](05_Medium_Ultra/README.md) | [Ergebnisse](05_Medium_Ultra/Ergebnisse/summary.md) |

[Direkte Zuordnung aller Haupt-Runner und Auswertungsskripte](RUNNER_UEBERSICHT.md)

## Gleicher Aufbau jeder Reihe

```text
Versuchsreihe/
├── README.md
├── Runner/                  Einstiegsskripte dieser Reihe
│   └── Hilfsmodule/         Gemeinsam genutzte interne Implementierung
├── Auswertung/              Skripte für die Ergebnisberechnung
│   └── Hilfsmodule/
├── Konfiguration/           Parameter, Eingaben und historische Quellstände
├── Laeufe/                  Nur die ausgewerteten Endversuche/Statusdateien
│   └── Variante/[Reasoning]/Aufgaben_001-100/Aufgabe_001/
└── Ergebnisse/              Finale MD-, JSON- und CSV-Berichte
```

`00_Gemeinsame_Dateien/` enthält Benchmarkdateien, Aufgabenauswahl und das
AgentCompass-Quellpaket.

Quellen, Prompts, Ergebnisse und Reports wurden inhaltlich nicht umgeschrieben.
Alte absolute Pfade und relative Quellenlinks in Originalberichten beziehen sich
weiterhin auf das ursprüngliche Labor.

Die Runner sind hier zur Dokumentation ihrer Zuordnung und ihres Codes geordnet.
Ihre historischen Pfadannahmen wurden nicht verändert; die neue Ordnerstruktur ist
kein unverändert ausführbares Ersatz-Labor. Es wurden keine neuen Experimente
oder Bewertungen gestartet. Alle Originale im ursprünglichen Labor bleiben erhalten.

## Abgeleiteter GSD-Workflow

[06_GSD_Workflow](06_GSD_Workflow/README.md) enthält den aktuell installierten
`guided-software-development`-Skill mit seinen fünf Unter-Skills, Referenzen,
Vorlagen und lokalen Prüftests. Der Ordner dokumentiert den abgeleiteten Workflow
und ist keine zusätzliche Benchmark-Versuchsreihe.

## Anforderungsaufnahme

[07_Anforderungsaufnahme] enthält die übergebenen Dateien für die Anforderungsaufnahme.
Darunter sind Mockups sowie Anforderungen und die Aufteilung der Funktionen über die 
zwei Systeme Theo und Dynamics 365 Sales.
