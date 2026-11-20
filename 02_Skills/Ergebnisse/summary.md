# Skill-Untersuchung: Sol 6 / medium

Bewertbare Aufgaben im bisherigen Bericht: 290; Ausschlüsse: [40, 65, 127, 184, 186, 217, 218, 258, 261, 285].
Alle ausgewählten Versuche abgeschlossen: True; vollständige Reihe 1–300: True.

| Variante | Abgeschlossen | Gelöst / bewertbar | Lösungsquote | Bekannte Input + Output, Mio. | Tokens vollständig | Modellzeit, min. |
|---|---:|---:|---:|---:|---|---:|
| standard | 290/290 | 168/290 | 57,93 % | 240.62 | True | 831.7 |
| tdd | 290/290 | 172/290 | 59,31 % | 480.64 | True | 1447.9 |
| debugging | 290/290 | 167/290 | 57,59 % | 328.35 | True | 1058.9 |
| verification | 290/290 | 163/290 | 56,21 % | 278.31 | True | 935.7 |

Lösungsquote = gelöste Aufgaben / bewertbare Aufgaben × 100. Der Nenner beträgt je Variante 290; die 10 ausgeschlossenen Aufgaben zählen nicht dazu. Bei offenen oder technisch unterbrochenen Versuchen wird noch keine endgültige Quote ausgewiesen.
Jede Variante startet frisch mit demselben Snapshot. Alle verwenden Sol 6 / medium, Abo-Anmeldung, dieselben Offline-Regeln und den unveränderten offiziellen Evaluator.
Die drei angepassten Superpowers-Anweisungspakete überschneiden sich. Ergebnisse isolieren keine einzelnen Mechanismen und reproduzieren nicht den tdd-workflow von Han et al.
Die Modellwahl erfolgte auf bereits bekannten Aufgaben. Die Reihe untersucht Zusatznutzen auf diesem Aufgabensatz; sie ist kein unabhängiger Test auf neuen Aufgaben.

## Gepaarte Vergleiche gegen Standard

| Skill | Unterschied, Prozentpunkte | 95%-Intervall | McNemar p | Holm p |
|---|---:|---|---:|---:|
| tdd | 1.38 | [-1.72; 4.48] | 0.503445 | 1.000000 |
| debugging | -0.34 | [-2.76; 2.07] | 1.000000 | 1.000000 |
| verification | -1.72 | [-4.48; 0.69] | 0.301758 | 0.905273 |

Intervalle: gepaarter Aufgaben-Bootstrap, 10.000 Ziehungen, feste Seeds, unadjustierte 95%-Intervalle. Holm korrigiert die drei p-Werte; keine Repository-Clusterkorrektur.

## Skill-Befolgung und Protokolle

skill-loading.json belegt die vollständige Einfügung in die Modellanweisungen. Das beweist keine Befolgung.
skill-observations.json enthält konservative Beobachtungen aus Ereignissen, keine automatischen Compliance-Urteile. Nicht erkannte Shell-/Code-Mode-Aktionen bleiben unklar.
Manuelle Bewertungen stehen gegebenenfalls in skill-review.json pro Versuch und benötigen Belegstellen. Fehlende Bewertungen bleiben pending, technische Hindernisse werden getrennt von Nichtbefolgung erfasst.

## Zusätzlicher Aufwand durch Unterbrechungen

Archivierte Modellstufen: 8; davon Nutzung unbekannt/unvollständig: 8.
Bekannte zusätzliche Input + Output: 0 Tokens.
Die Haupttabelle enthält nur aktive Endversuche; archivierte Anläufe sind separat ausgewiesen. Fehlende Tokenwerte sind unbekannt, nicht null.
Cache-Tokens sind Teil der Eingabe, Reasoning-Tokens Teil der Ausgabe. Es werden keine API-Kosten oder Abo-Prozente daraus abgeleitet.

[Vollständige Daten](summary.json) · [Aufgaben](tasks.csv) · [Variantenübersicht](variants.csv)
