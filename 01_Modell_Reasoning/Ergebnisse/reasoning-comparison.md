# Vergleich der Reasoning-Stufen – Aufgaben 1–300

Architektur: ausschließlich Standard. low, medium, high, xhigh und max sind enthalten, sofern Ergebnisse vorhanden sind.

medium umfasst die Standard-Abgaben aus den ursprünglichen Architektur-Batches: Luna Aufgaben 1–20 aus experiment-luna-01 und 21–100 aus experiment-luna-100; Sol Aufgaben 1–20 aus experiment-v2-repeat-01 und 21–100 aus experiment-sol-100. Rollen-B-Ergebnisse werden nicht in eine Standard-Konfiguration gemischt. Für Aufgaben ab 101 stammen die medium-Ergebnisse aus den jeweiligen experiment-reasoning-Ordnern. Jede aktive Abgabe wird genau einmal verwendet; technische Archive sind keine zusätzlichen Versuche in der Ergebnisquote.

Versionszuordnung: Die historischen Sol-Reihen verwenden gpt-6.1-sol. Neue gpt-6-sol-Reihen stehen separat unter experiment-reasoning-sol6-*; ihre medium-Referenzen stammen aus experiment-reasoning-sol6-medium beziehungsweise aus vorhandenen Standard-Architektur-Batches. Die Generationen werden niemals zusammengeführt oder umbenannt.

## Tokenverbrauch und % gelöst

Basis: dieselben 281 offiziell bewerteten Aufgaben je Konfiguration. Tokenverbrauch = Input + Output inklusive gecachtem Input. Davon cached = bereits im Input enthaltene gecachte Tokens; ≥ kennzeichnet unvollständige Tokenzähler.

| Modell     | Reasoning | Tokenverbrauch (Mio.) | Davon cached (Mio.) | % gelöst |
| ---------- | --------- | --------------------: | ------------------: | -------: |
| gpt-6-luna | low       |                185.90 |              173.00 |    49.1% |
| gpt-6-luna | medium    |                140.18 |              127.70 |    52.7% |
| gpt-6-luna | high      |                227.35 |              210.42 |    55.5% |
| gpt-6-luna | xhigh     |                454.04 |              428.20 |    58.0% |
| gpt-6-luna | max       |                489.12 |              460.94 |    58.4% |
| gpt-6-sol  | low       |                132.22 |              123.95 |    57.3% |
| gpt-6-sol  | medium    |                250.88 |              238.24 |    58.7% |
| gpt-6-sol  | high      |                338.99 |              322.64 |    56.6% |
| gpt-6-sol  | xhigh     |                408.14 |              388.74 |    57.3% |
| gpt-6-sol  | max       |                546.91 |              521.34 |    57.3% |

## Gesamtübersicht: alle Aufgaben 1–300

Alle 300 ausgewählten Aufgaben pro Konfiguration werden ausgewiesen. Fehlende Ergebnisse, Kontrollausschlüsse und ungültige Exporte bleiben als solche sichtbar; sie werden nicht als bewertete Lösungsfehler umgedeutet.

| Modell | Reasoning | Aufgaben | Gelöst | Offiziell bewertet | Ungültig | Leer | Ausgeschlossen | Fehlend | Input + Output (Mio.) | Vollständige Zähler |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gpt-6-luna | low | 300 | 141 | 284 | 4 | 2 | 10 | 0 | 190.88 | 290/290 |
| gpt-6-luna | medium | 300 | 149 | 284 | 4 | 1 | 10 | 1 | 144.59 | 289/289 |
| gpt-6-luna | high | 300 | 158 | 285 | 5 | 0 | 10 | 0 | 237.24 | 290/290 |
| gpt-6-luna | xhigh | 300 | 165 | 285 | 5 | 0 | 10 | 0 | 472.70 | 290/290 |
| gpt-6-luna | max | 300 | 166 | 285 | 5 | 0 | 10 | 0 | 506.44 | 290/290 |
| gpt-6-sol | low | 300 | 163 | 285 | 5 | 0 | 10 | 0 | 137.31 | 290/290 |
| gpt-6-sol | medium | 300 | 167 | 285 | 5 | 0 | 10 | 0 | 259.88 | 290/290 |
| gpt-6-sol | high | 300 | 161 | 285 | 5 | 0 | 10 | 0 | 349.56 | 290/290 |
| gpt-6-sol | xhigh | 300 | 162 | 285 | 5 | 0 | 10 | 0 | 426.10 | 290/290 |
| gpt-6-sol | max | 300 | 163 | 285 | 5 | 0 | 10 | 0 | 569.03 | 290/290 |

Die unterschiedlichen Mengen bewerteter Abgaben erklären, warum die Rohzahlen oben nicht direkt identische Nenner haben. Alle Einzelaufgaben einschließlich Status und Herkunft stehen in [reasoning-tasks.csv](reasoning-tasks.csv).

## Gepaarter Vergleich: dieselben 281 Aufgaben aus 1–300

Nur Aufgaben, für die jede Konfiguration ein offizielles Bewertungsergebnis hat. Nicht enthalten: [14, 31, 40, 65, 88, 101, 127, 184, 186, 195, 210, 217, 218, 237, 258, 261, 279, 281, 285]. Vereinbarte Kontrollausschlüsse im gewählten Bereich: [40, 65, 127, 184, 186, 217, 218, 258, 261, 285]; andere Fälle fehlen oder haben ungültige Exporte in mindestens einer Variante. Die ersten 20 Aufgaben sind in diesem Vergleich enthalten, soweit sie diese Bedingung erfüllen.

| Modell | Reasoning | Gelöst | Quote | Input + Output (Mio.) | Nicht gecachter Input (Mio.) | Ø Rollenzeit (min) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| gpt-6-luna | low | 138/281 | 49.1% | 185.90 | 11.76 | 1.63 |
| gpt-6-luna | medium | 148/281 | 52.7% | 140.18 | 11.36 | 2.29 |
| gpt-6-luna | high | 156/281 | 55.5% | 227.35 | 14.85 | 2.33 |
| gpt-6-luna | xhigh | 163/281 | 58.0% | 454.04 | 20.69 | 3.94 |
| gpt-6-luna | max | 164/281 | 58.4% | 489.12 | 21.83 | 4.31 |
| gpt-6-sol | low | 161/281 | 57.3% | 132.22 | 7.25 | 1.60 |
| gpt-6-sol | medium | 165/281 | 58.7% | 250.88 | 10.67 | 2.56 |
| gpt-6-sol | high | 159/281 | 56.6% | 338.99 | 13.51 | 3.22 |
| gpt-6-sol | xhigh | 161/281 | 57.3% | 408.14 | 15.71 | 3.88 |
| gpt-6-sol | max | 161/281 | 57.3% | 546.91 | 20.13 | 5.75 |

Die Quote misst das Bestehen offizieller Pflicht-Tests. Sie isoliert nicht in jedem Fall die Fähigkeiten der Agenten; bekannte Testdaten-/Schnittstellenprobleme bleiben erhalten.

## Gepaarte statistische Vergleiche

| Vergleich | Nur erste Stufe gelöst | Nur zweite Stufe gelöst | Exakter McNemar-p-Wert | Holm-korrigiert |
| --- | ---: | ---: | ---: | ---: |
| gpt-6-luna/low vs gpt-6-luna/medium | 13 | 23 | 0.1325 | 1.0000 |
| gpt-6-luna/low vs gpt-6-luna/high | 11 | 29 | 0.0064 | 0.1093 |
| gpt-6-luna/low vs gpt-6-luna/xhigh | 10 | 35 | 0.0002 | 0.0047 |
| gpt-6-luna/low vs gpt-6-luna/max | 10 | 36 | 0.0002 | 0.0031 |
| gpt-6-luna/medium vs gpt-6-luna/high | 10 | 18 | 0.1849 | 1.0000 |
| gpt-6-luna/medium vs gpt-6-luna/xhigh | 8 | 23 | 0.0107 | 0.1708 |
| gpt-6-luna/medium vs gpt-6-luna/max | 6 | 22 | 0.0037 | 0.0669 |
| gpt-6-luna/high vs gpt-6-luna/xhigh | 6 | 13 | 0.1671 | 1.0000 |
| gpt-6-luna/high vs gpt-6-luna/max | 6 | 14 | 0.1153 | 1.0000 |
| gpt-6-luna/xhigh vs gpt-6-luna/max | 6 | 7 | 1.0000 | 1.0000 |
| gpt-6-sol/low vs gpt-6-sol/medium | 3 | 7 | 0.3438 | 1.0000 |
| gpt-6-sol/low vs gpt-6-sol/high | 10 | 8 | 0.8145 | 1.0000 |
| gpt-6-sol/low vs gpt-6-sol/xhigh | 9 | 9 | 1.0000 | 1.0000 |
| gpt-6-sol/low vs gpt-6-sol/max | 9 | 9 | 1.0000 | 1.0000 |
| gpt-6-sol/medium vs gpt-6-sol/high | 11 | 5 | 0.2101 | 1.0000 |
| gpt-6-sol/medium vs gpt-6-sol/xhigh | 10 | 6 | 0.4545 | 1.0000 |
| gpt-6-sol/medium vs gpt-6-sol/max | 10 | 6 | 0.4545 | 1.0000 |
| gpt-6-sol/high vs gpt-6-sol/xhigh | 7 | 9 | 0.8036 | 1.0000 |
| gpt-6-sol/high vs gpt-6-sol/max | 5 | 7 | 0.7744 | 1.0000 |
| gpt-6-sol/xhigh vs gpt-6-sol/max | 3 | 3 | 1.0000 | 1.0000 |

Explorative Tests mit Holm-Korrektur über alle dargestellten Vergleiche, einschließlich high und xhigh. Nicht signifikant bedeutet nicht gleichwertig. Dies sind einzelne Versuche pro Aufgabe/Konfiguration.

## Interpretation

- gpt-6-luna: low: 138/281; medium: 148/281; high: 156/281; xhigh: 163/281; max: 164/281.
- gpt-6-sol: low: 161/281; medium: 165/281; high: 159/281; xhigh: 161/281; max: 161/281.

Höheres Reasoning garantiert keine höhere Quote: high und max können ähnliche Ergebnisse liefern, und einzelne Stufen können schlechter abschneiden als medium. Tokenaufwand und Zeit sind deshalb neben der Lösungsquote zu betrachten.

## Vergleichbarkeit und Herkunft

- medium setzt sich aus historischen Standard-Batches zusammen. Gleiche Architektur, Modell-ID und Reasoning-Stufe bedeuten keine vollständig identische technische Durchführung: Workerzahlen, Neustarts und frühere Harness-Stände unterscheiden sich.
- Rollenzeit umfasst Wartezeit und lokale Tests; sie ist nicht CPU-Zeit oder Gesamtdauer paralleler Batches. Alte Zeitlimit-/Abbruchereignisse schränken die Zeitvergleiche zusätzlich ein.
- Tokenwerte umfassen aktive Abgaben, nicht archivierte Anläufe. Cached Input ist bereits im Input enthalten. Ein Abo-Prozentsatz lässt sich nicht zuverlässig ableiten.
- Bekannte Fälle: 14/88 Redis-Dateien im Export; 25/81 Fixtures im Referenz- statt Testpatch; 57 Mischfall einer genannten Fixture; 87 widersprüchliche Schnittstellenpfade; 99 Abhängigkeiten/Checksummen. Keine neuen Ausschlüsse, Patchreparaturen oder Testläufe für diesen Report.

[Maschinenlesbare Auswertung mit Quellenhashes](reasoning-comparison.json) · [Alle Aufgaben und Herkunft](reasoning-tasks.csv)

## Verwendete Batches

- [gpt-6-luna/low: experiment-reasoning-luna-low/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-low/batch-01/manifest.json)
- [gpt-6-luna/low: experiment-reasoning-luna-low/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-low/batch-02/manifest.json)
- [gpt-6-luna/low: experiment-reasoning-luna-low/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-low/batch-03/manifest.json)
- [gpt-6-luna/medium: experiment-luna-01/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-luna-01/batch-01/manifest.json)
- [gpt-6-luna/medium: experiment-luna-01/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-luna-01/batch-02/manifest.json)
- [gpt-6-luna/medium: experiment-luna-100/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-luna-100/batch-01/manifest.json)
- [gpt-6-luna/medium: experiment-reasoning-luna-medium/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-medium/batch-02/manifest.json)
- [gpt-6-luna/medium: experiment-reasoning-luna-medium/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-medium/batch-03/manifest.json)
- [gpt-6-luna/high: experiment-reasoning-luna-high/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-high/batch-01/manifest.json)
- [gpt-6-luna/high: experiment-reasoning-luna-high/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-high/batch-02/manifest.json)
- [gpt-6-luna/high: experiment-reasoning-luna-high/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-high/batch-03/manifest.json)
- [gpt-6-luna/xhigh: experiment-reasoning-luna-xhigh/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-xhigh/batch-01/manifest.json)
- [gpt-6-luna/xhigh: experiment-reasoning-luna-xhigh/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-xhigh/batch-02/manifest.json)
- [gpt-6-luna/xhigh: experiment-reasoning-luna-xhigh/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-xhigh/batch-03/manifest.json)
- [gpt-6-luna/max: experiment-reasoning-luna-max/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-max/batch-01/manifest.json)
- [gpt-6-luna/max: experiment-reasoning-luna-max/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-max/batch-02/manifest.json)
- [gpt-6-luna/max: experiment-reasoning-luna-max/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-luna-max/batch-03/manifest.json)
- [gpt-6-sol/low: experiment-reasoning-sol6-low/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-low/batch-01/manifest.json)
- [gpt-6-sol/low: experiment-reasoning-sol6-low/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-low/batch-02/manifest.json)
- [gpt-6-sol/low: experiment-reasoning-sol6-low/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-low/batch-03/manifest.json)
- [gpt-6-sol/medium: experiment-reasoning-sol6-medium/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-medium/batch-01/manifest.json)
- [gpt-6-sol/medium: experiment-reasoning-sol6-medium/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-medium/batch-02/manifest.json)
- [gpt-6-sol/medium: experiment-reasoning-sol6-medium/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-medium/batch-03/manifest.json)
- [gpt-6-sol/high: experiment-reasoning-sol6-high/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-high/batch-01/manifest.json)
- [gpt-6-sol/high: experiment-reasoning-sol6-high/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-high/batch-02/manifest.json)
- [gpt-6-sol/high: experiment-reasoning-sol6-high/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-high/batch-03/manifest.json)
- [gpt-6-sol/xhigh: experiment-reasoning-sol6-xhigh/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-xhigh/batch-01/manifest.json)
- [gpt-6-sol/xhigh: experiment-reasoning-sol6-xhigh/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-xhigh/batch-02/manifest.json)
- [gpt-6-sol/xhigh: experiment-reasoning-sol6-xhigh/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-xhigh/batch-03/manifest.json)
- [gpt-6-sol/max: experiment-reasoning-sol6-max/batch-01/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-max/batch-01/manifest.json)
- [gpt-6-sol/max: experiment-reasoning-sol6-max/batch-02/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-max/batch-02/manifest.json)
- [gpt-6-sol/max: experiment-reasoning-sol6-max/batch-03/manifest.json](/home/joelborges-ximenes/swebench-pro-verified-lab/experiment-reasoning-sol6-max/batch-03/manifest.json)
