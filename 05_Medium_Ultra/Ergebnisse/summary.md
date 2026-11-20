# Gesamtbericht: Sol 6 medium versus natives Ultra

## Ergebnis

Medium löst **172/290**, Ultra **170/290** Aufgaben. Die Differenz Ultra minus Medium beträgt **-0.69 Prozentpunkte**.
Der gepaarte exakte zweiseitige McNemar-Test ergibt **p = 0.8145**.
Es zeigt sich kein statistisch signifikanter Lösungsvorteil von Ultra. Das ist kein Nachweis einer Gleichwertigkeit.
Ultra benötigt etwa **2.10-mal so viel Modellprozesszeit**. Der protokollierte Tokenverbrauch beträgt **mindestens 4.37-mal** den Medium-Verbrauch; bei Ultra ist er unvollständig.

## Umfang und Aufbau

Alle drei Batches sind abgeschlossen: 300 ausgewählte Aufgaben, zehn gemeinsame genehmigte Kontrollausschlüsse,
**290 bewertbare Aufgaben und 580 abgeschlossene Endversuche**. Die Ausschlüsse sind 40, 65, 127, 184, 186, 217, 218, 258, 261, 285.
Es werden ausschließlich die neuen Medium- und Ultra-Ergebnisse dieser Reihe verglichen. Frühere Reasoning- oder MAS-Ergebnisse werden nicht beigemischt.
Beide Arme starten je Aufgabe mit einem frischen Hauptkontext und Container. Nur kontrollvalidierte Umgebungen werden wiederverwendet.
Pro Aufgabe verwenden beide Arme identische vorbereitete Modell-Images und identische offizielle Evaluations-Images.
Medium nutzt Reasoning medium ohne native Agenten. Ultra kombiniert Reasoning ultra mit nativer Orchestrierung und einem entsprechenden Delegationsprompt.
Der Vergleich isoliert deshalb weder den Reasoning-Effekt noch den Multiagenten-Effekt.
Fünf Worker laufen für beide Arme zusammen. Pro Versuch gelten 4 CPUs und 8 GiB RAM; native Kinder teilen diesen Container.
Unteragenten können Elternkontext übernehmen; dies entspricht nicht dem frischen, separat isolierten Rollenkontext des früheren Rollen-B/C-Aufbaus.
Authentifizierung erfolgt über das Abo, externe Recherche ist gesperrt. Es gibt keine Modellzeitgrenze und kein angeglichenes Tokenbudget.

## Ergebnisse je Aufgabenblock

| Aufgaben | Bewertbar | Medium gelöst | Ultra gelöst |
|---|---:|---:|---:|
| 1–100 | 98 | 62 | 63 |
| 101–200 | 97 | 49 | 46 |
| 201–300 | 95 | 61 | 61 |

## Lösungsquote, Verbrauch und Dauer

| Variante | Gelöst | Quote | Bekannte Eingabe + Ausgabe, Mio. | Ø Modellprozesszeit | Median | Vollständige Nutzung |
|---|---:|---:|---:|---:|---:|---:|
| medium | 172/290 | 59.3% | 244.49 | 2.60 min | 2.41 min | 290/290 |
| ultra | 170/290 | 58.6% | 1069.06 | 5.45 min | 5.21 min | 275/290 |

| Variante | Eingabe, Mio. | Davon Cache, Mio. | Ungecachte Eingabe, Mio. | Ausgabe, Mio. | Summierte Prozesszeit |
|---|---:|---:|---:|---:|---:|
| medium | 242.46 | 231.62 | 10.85 | 2.03 | 12.57 h |
| ultra | 1060.72 | 1019.40 | 41.31 | 8.34 | 26.36 h |

Cache-Tokens sind bereits in der Eingabe enthalten und werden nicht nochmals addiert. Reasoning-Ausgaben sind Teil der Ausgabe.
Die Tokenwerte stammen aus eindeutigen Thread-Zählern; Eltern-CLI-Nutzung wird nicht zusätzlich zum gleichen Rollout-Thread addiert.
Dies sind keine Abo-Prozente oder API-Kosten. Bei Ultra handelt es sich um bekannte Mindestwerte, nicht um eine vollständige Abrechnung.
Prozesszeiten enthalten das Warten des Hauptagenten auf Kinder. Parallele Kinderzeiten werden nicht nochmals addiert.
Die Summe ist keine Kalenderlaufzeit bei fünf Workern. Containeraufbau, nachträglicher Protokollexport und offizielle Bewertung sind darin nicht enthalten.
Archivierte technische Fehlstarts sind nicht Bestandteil der Endversuchs-Tabelle.

## Gepaarte Aufgabenergebnisse

Nur Medium gelöst: **10 Aufgaben** – [35, 74, 75, 119, 121, 144, 208, 209, 221, 268].
Nur Ultra gelöst: **8 Aufgaben** – [18, 41, 78, 82, 215, 252, 284, 296].
Bei 272 Aufgaben stimmen die binären Lösungsergebnisse überein.
Der primäre Test verwendet diese gepaarten Unterschiede, nicht einen ungepaarten Vergleich zweier Quoten.
Es gibt einen primären Gesamtvergleich. Die Blocktabelle ist deskriptiv; einzelne Blöcke sind keine unabhängigen Bestätigungsstudien.

## Tatsächliche native Delegation

Nachgewiesen sind **mindestens 667 Kind-Threads bei mindestens 275 von 290 Ultra-Aufgaben**.
Die Kennzeichnung „mindestens“ berücksichtigt die 15 Aufgaben mit fehlendem Rollout-Export. Null beobachtete Kinder bei diesen Aufgaben bedeutet unbekannt, nicht keine Delegation.
Thread-IDs, Rollenpfade, Elternbeziehungen, Tiefe, beobachtete Modelle/Reasoning-Stufen und Protokollquellen stehen in `agents.csv`.
Die frei benannten Rollenpfade sind keine standardisierte Rollentaxonomie. Eine Häufigkeit von Delegation weist allein keinen kausalen Nutzen nach.
Anders als beim früheren freiwilligen Organizer wurden native Unteragenten in dieser Reihe auf einem großen Teil der Aufgaben tatsächlich genutzt.

## Einschränkung der Token- und Delegationsprotokolle

Bei **15 Ultra-Aufgaben** konnte der Hilfsprozess die Sitzungsdateien nicht exportieren:
`AttributeError: PosixPath object has no attribute is_relative_to`.
Der Exportcode verwendete eine Methode, die der ältere Python-Interpreter dieser Images nicht anbietet. Dies ist ein Fehler im Protokollierungshelfer.
Betroffene Aufgaben: 4, 27, 37, 56, 64, 110, 126, 131, 145, 153, 157, 185, 188, 196, 270.
Der Fehler trat nach dem Modellprozess beim Einsammeln der Logs auf. Die offiziellen Auswertungen und finalen Patches liegen vor;
der Lösungsvergleich verwendet weiterhin alle 290 Aufgaben. Für diese 15 Aufgaben ist nur die Eltern-CLI-Nutzung erfasst;
möglicher zusätzlicher Unteragentenverbrauch und deren vollständige Rollenprotokolle fehlen. Es wurden keine Aufgaben deswegen nachträglich ausgeschlossen.
Für Folgeversuche sollte der Export kompatibel mit den älteren Python-Versionen umgesetzt werden; dieser Bericht verändert keine historischen Dateien.

## Technische Prüfung und Wiederaufnahmen

Geprüft wurden 290 bestandene Kontrollpaare, 580 offizielle Endbewertungen und 580 Modellstufen.
Die Ergebniswerte stimmen mit den offiziellen Bewertungen überein. Alle Endversuche haben Status completed, alle geprüften Modellstufen Exitcode 0 und keine Modelltimeouts oder unerwarteten Webtools.
„Gelöst“ bezieht sich auf die offiziellen Pflicht-Testmengen; es bedeutet nicht zwangsläufig, dass jeder zusätzliche Repository-Test besteht.
Aufgabenidentitäten, angeforderte Modelle/Reasoning-Stufen, Authentifizierung und verwendete Image-IDs wurden geprüft.
Shared-Runner, native Ultra-Implementierung, Runtime-Profil und Codex-Binärdateien stimmen über die Batches überein.
Der Einstiegsrunner hat zwei eingefrorene Versionen: Für batch-01 wurden Routing auf Aufgaben 1–100 und validierte Kontrollspender ergänzt.
Die ausführenden Funktionen models/resume/validate/capsule und die native Modellintegration sind identisch; Quellversionen bleiben dokumentiert.
Rollout-Prüfung: 942 Dateien; beobachtete Modelle: {'gpt-6-sol': 942}; beobachtetes Reasoning: {'ultra': 942}.
Bei 942 Rollouts beginnt der kumulative Zähler beim ersten eigenen Modellaufruf.
Es gibt 2 Wiederaufnahme-Archive und 264 eindeutige archivierte Fehlermeldungen nach Deduplizierung.
Die Unterbrechungsarchive werden nicht als zusätzliche unabhängige Versuche gezählt. Fertige Ergebnisse bleiben auch bei Nichtlösung erhalten;
es erfolgt keine Best-of-Auswahl nach Benchmark-Score. Teilweise gelöschte Docker-Images verhindern eine sofortige exakte Wiederholung aller alten Umgebungen.

## Interpretation

Unter den untersuchten Bedingungen liefert Ultra trotz deutlich höherem protokolliertem Aufwand keinen beobachteten Lösungsvorteil gegenüber Medium.
Das Ergebnis spricht für Medium als sparsamere Referenz in dieser Untersuchung. Es beweist weder allgemeine Wirkungslosigkeit von Multiagentensystemen
noch einen generellen Nachteil von Ultra. Der kombinierte Eingriff aus höherem Reasoning, Delegation und zusätzlichem Prompt lässt die Einzelursachen offen.
Es gibt einen Endversuch je Aufgabe/Variante. Aufgaben desselben Repositories können abhängig sein; der McNemar-Test berücksichtigt keine Repository-Cluster.
Modellwahl und Setup entstanden nach früheren Experimenten mit überlappenden Aufgaben. Dies ist eine explorative Auswertung und kein unabhängiger Holdout-Test.

## Reproduktion und Daten

Aus dem Laborordner: `.venv/bin/python compare_sol_ultra_all.py`.
[Maschinenlesbarer Bericht und Prüfsummen](summary.json) · [Alle 300 Aufgaben](tasks.csv) · [Beobachtete Unteragenten](agents.csv)

- [batch-01](../../experiment-sol6-medium-ultra/batch-01/manifest.json)
- [batch-02](../../experiment-sol6-medium-ultra/batch-02/manifest.json)
- [batch-03](../../experiment-sol6-medium-ultra/batch-03/manifest.json)
