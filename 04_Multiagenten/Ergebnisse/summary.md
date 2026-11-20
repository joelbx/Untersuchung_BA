# Architekturvergleich: Sol 6 / medium, Aufgaben 1–300

Alle drei Batches sind abgeschlossen. Zehn vorab genehmigte Kontrollausschlüsse gelten für alle Varianten:
40, 65, 127, 184, 186, 217, 218, 258, 261, 285. Damit umfasst der Vergleich 290 Aufgaben je Architektur und 870 Endversuche.

## Ergebnisse und Aufwand

| Architektur | Gelöst | Quote | Eingabe + Ausgabe, Mio. | Tokenfaktor zu Standard | Ø Modellzeit je Aufgabe |
|---|---:|---:|---:|---:|---:|
| Standard | 166/290 | 57.2% | 230.03 | 1.00 | 2.84 min |
| Rollen B | 165/290 | 56.9% | 474.95 | 2.06 | 6.76 min |
| Organizer | 166/290 | 57.2% | 245.50 | 1.07 | 3.05 min |

Tokenzahlen sind Eingabe einschließlich Cache-Tokens plus Ausgabe. Cache-Eingaben und Reasoning-Ausgaben
werden nicht doppelt addiert. Es handelt sich nicht um Aboprozente oder API-Kosten.
Enthalten ist die Nutzung der aktiven Endversuche; archivierte Unterbrechungen verursachten zusätzlichen Verbrauch.
Die Modellzeit summiert protokollierte Rollen-/Agentenzeiten, ohne Containerstart und offizielle Bewertung;
sie ist keine Gesamtlaufzeit bei fünf parallelen Workern.

| Architektur | Eingabe, Mio. | Davon Cache, Mio. | Ungecachte Eingabe, Mio. | Ausgabe, Mio. | Korrekturrunden |
|---|---:|---:|---:|---:|---:|
| Standard | 228.07 | 216.56 | 11.51 | 1.96 | 0 |
| Rollen B | 470.74 | 437.82 | 32.92 | 4.21 | 193 |
| Organizer | 243.41 | 231.48 | 11.94 | 2.08 | 0 |

## Einzelne Aufgabenblöcke

| Aufgaben | Bewertbar | Standard | Rollen B | Organizer |
|---|---:|---:|---:|---:|
| 1–100 | 98 | 63 | 60 | 63 |
| 101–200 | 97 | 47 | 47 | 44 |
| 201–300 | 95 | 56 | 58 | 59 |

## Gepaarte Vergleiche

Zweiseitiger exakter McNemar-Test auf denselben 290 Aufgaben; Holm-Korrektur für drei Architekturvergleiche.

| Vergleich | Nur links gelöst | Nur rechts gelöst | p exakt | p Holm |
|---|---:|---:|---:|---:|
| standard vs roles-b | 8 | 7 | 1.0000 | 1.0000 |
| standard vs self-organizing | 4 | 4 | 1.0000 | 1.0000 |
| roles-b vs self-organizing | 9 | 10 | 1.0000 | 1.0000 |

Keiner der Vergleiche zeigt einen statistisch signifikanten Lösungsunterschied.
Das beweist keine Gleichwertigkeit. Es gibt nur einen Endversuch pro Aufgabe und Architektur;
Modellstreuung wird nicht durch Wiederholungen geschätzt. Aufgaben innerhalb desselben Repositories
können abhängig sein; diese Tests sind explorativ und berücksichtigen solche Cluster nicht.

## Tatsächliche Delegation

Der Organizer erzeugte 3 Unteragenten bei 2 von 290 Aufgaben.
Aufgabe 46: Python module dependency resolver implementer. Aufgabe 257: Go service listener specialist
und Go tsh CLI implementation specialist. Alle drei Vorschläge wurden übernommen; beide Aufgaben blieben ungelöst.
Bei den übrigen 288 Aufgaben arbeitete der Koordinator ohne Unteragenten.

Der Vergleich untersucht daher vor allem die freiwillige Nutzung einer Delegationsmöglichkeit.
Er erlaubt keine belastbare Aussage über den Nutzen regelmäßig tatsächlich eingesetzter Unteragenten.
Auch ohne Delegation unterscheidet sich der Koordinator-Prompt von Standard.

## Prüfung und Grenzen

Geprüft: 290 bestandene Original-/Referenzkontrollen, 870 offizielle Bewertungen und 1646 abgeschlossene Modellstufen.
Alle Endversuche haben Status completed; die Ergebniswerte stimmen mit den offiziellen Bewertungen überein.
Alle geprüften Stufen melden vollständige Nutzung, Exitcode 0, keine Modelltimeouts und keine unerwarteten Webtools.
Aufgabenidentitäten stimmen mit der Masterauswahl überein; alle Architekturen verwenden je Aufgabe dasselbe vorbereitete Image.
Modell/Reasoning, eingefrorene Ausführungsquellen, Architekturregeln und Codex-Binärdateien stimmen über alle drei Batches überein.
Die Bewertung folgt den offiziellen Pflicht-Testmengen; resolved bedeutet nicht, dass jeder beliebige Repository-Test besteht.
Diese Prüfung ersetzt keine manuelle Ursachenanalyse sämtlicher ungelöster Aufgaben.

Technische Unterbrechungen und Wiederaufnahmen bleiben archiviert. Der Bericht wählt ausschließlich den aktiven Endversuch,
keine Best-of-Auswahl historischer Kandidaten. Images aus abgeschlossenen Aufgaben wurden teilweise gelöscht;
Logs und Nachweise bleiben erhalten, eine exakte sofortige Wiederholung aller alten Umgebungen ist damit nicht möglich.
Es gibt kein angeglichenes Tokenbudget. Pro Container gelten gleiche Limits, der Organizer kann gleichzeitig
einen Hauptagenten- und einen Unteragenten-Container halten. Modell/Reasoning wurden nach einer früheren
Reasoning-Untersuchung auf überlappenden Aufgaben gewählt; der Vergleich ist explorativ und kein unabhängiger Holdout-Test.

## Interpretation

Standard und Organizer erreichen jeweils 166 Lösungen, Rollen B 165. Rollen B benötigt deutlich mehr Tokens und Modellzeit,
ohne dass sich hier eine höhere Lösungsquote zeigt. Standard ist unter diesen Versuchsbedingungen die sparsamste
der drei Varianten bei gleicher beobachteter Lösungsquote wie der Organizer.
Aus diesem Ergebnis folgt keine allgemeine Wirkungslosigkeit von Multiagentensystemen.

## Reproduktion und Nachweise

Erneut erzeugen: `.venv/bin/python compare_mas_300.py` aus dem Laborordner.
[Maschinenlesbare Daten, Prüfungen und Quell-Prüfsummen](summary.json) · [Alle Aufgaben](tasks.csv) · [Delegationen](delegations.csv)

- [experiment-mas-sol6-medium/batch-01](../../experiment-mas-sol6-medium/batch-01/manifest.json)
  - [Unterbrechungsarchiv](../../experiment-mas-sol6-medium/batch-01/technical-interruptions/control-repair-20261021T064817-59f4b8/)
  - [Unterbrechungsarchiv](../../experiment-mas-sol6-medium/batch-01/technical-interruptions/control-repair-20261021T063023-0c8a6c/)
  - [Unterbrechungsarchiv](../../experiment-mas-sol6-medium/batch-01/technical-interruptions/model-resume-20261021T143529-5f338e/)
- [experiment-mas-sol6-medium/batch-02](../../experiment-mas-sol6-medium/batch-02/manifest.json)
  - [Unterbrechungsarchiv](../../experiment-mas-sol6-medium/batch-02/technical-interruptions/model-resume-20261022T125721-a04c6d/)
- [experiment-mas-sol6-medium-300/batch-03](../../experiment-mas-sol6-medium-300/batch-03/manifest.json)
  - [Unterbrechungsarchiv](../../experiment-mas-sol6-medium-300/batch-03/technical-interruptions/model-resume-20261021T222100-553b2b/)
