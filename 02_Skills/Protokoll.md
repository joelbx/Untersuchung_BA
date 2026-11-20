# Skill-Untersuchung: festgelegtes Protokoll

Vier frische Bedingungen auf denselben Aufgaben: Standard ohne Zusatzskill,
Superpowers `test-driven-development`, `systematic-debugging` und
`verification-before-completion`. Modell immer **gpt-6-sol / medium**, lokale
Codex-Anmeldung über das Abo. Keine API-Schlüssel, keine menschliche Interaktion
während der Aufgabenbearbeitung, keine zusätzliche MAS-Architektur.

## Fragestellung und Hypothesen

Verbessern für autonomen Einsatz angepasste Superpowers-Skills die Reparaturleistung
gegenüber demselben Agenten ohne Zusatzskill, und welchen Aufwand verursachen sie?

| Bedingung | Vorab formulierte Hypothese |
|---|---|
| TDD | Ein vor Produktionsänderungen ausgeführter, passend fehlschlagender Test verbessert Korrektheit, erhöht möglicherweise Zeit und Tokens. |
| Systematic Debugging | Explizite Ursachenanalyse vor Reparaturen reduziert erfolglose Änderungsversuche und verbessert die Lösungsquote. |
| Verification Before Completion | Frische Prüfungen vor dem Abschluss reduzieren verbliebene Fehler und unbelegte Erfolgsmeldungen. |

Alle drei sind veröffentlichte Skills derselben Sammlung. Sie adressieren
unterschiedliche Schwerpunkte, überschneiden sich aber: TDD prüft ebenfalls,
Debugging enthält einen Reproduktionstest und abschließende Prüfung. Daher sind
dies **Vergleiche vollständiger Anweisungspakete**, keine isolierten Mechanismustests.
Die Prozesshypothese zu Reparaturversuchen benötigt manuelle Logbewertung;
eine Anzahl von Testbefehlen ist kein verlässlicher Ersatz für Reparaturversuche.

Quelle: <https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills>.
Originale, angepasste Dateien, SHA256-Werte, exakte Ersetzungen und Diffs liegen in
`skills-study/`. Nur benötigte Begleitdateien werden mitgeführt, keine
Upstream-Demonstrations-/Drucktests oder Entwicklungsprotokolle.

Die wissenschaftliche Auswahl beruht auf testgestützter Reparatur, Ursachenanalyse
und ausführungsbasierter Prüfung. Die Existenz dieser Methoden in der Literatur
belegt **nicht die Wirksamkeit genau dieser Superpowers-Dateien**.
Insbesondere wird nicht der `tdd-workflow` aus Han et al. reproduziert.
Han et al.: <https://arxiv.org/abs/2603.15401>;
Agentless: <https://arxiv.org/abs/2407.01489>;
Self-Debugging: <https://arxiv.org/abs/2304.05128>.

## Gemeinsame Versuchsregeln

- Aufgaben 1–300 aus der bestehenden eingefrorenen Auswahl. Ausschlüsse:
  **40, 65, 127, 184, 186, 217, 218, 258, 261, 285**. Keine Ersatzaufgaben.
  Insgesamt 290 bewertbare Aufgaben, 1.160 Endversuche.
- Ein frischer Modellversuch pro Aufgabe und Bedingung. Vorhandene Standard- oder
  MAS-Modellergebnisse werden weder übernommen noch Agenten bereitgestellt.
- Derselbe vorbereitete Snapshot pro Aufgabe für alle vier Bedingungen;
  eigener Container, eigenes CODEX_HOME, eigenes Arbeitsverzeichnis je Versuch.
- Vollständiger Skill-Text wird vor der ersten Aktion in die Developer-Anweisungen
  eingefügt. Das ist bewusste Zwangsanwendung, keine Untersuchung automatischer
  Skill-Entdeckung. Begleitdateien liegen nur im jeweiligen Container unter
  `/opt/experiment-skill`, außerhalb des exportierten Repositories.
- Standard erhält keinen Skill. Alle vier Bedingungen erhalten dieselbe knappe
  Autonomieregel: lokale Tests dürfen ergänzt werden, keine Rückfragen, keine
  Downloads, Prüfblocker und Unsicherheit dokumentieren, bestmöglichen Patch abgeben.
  Die alte Formulierung „existing tests only“ wird dafür in allen vier frischen
  Bedingungen gleich präzisiert. Dieser gemeinsame Zusatz steht im Runner als COMMON.
- Menschliche Eskalationen der Skills werden durch dokumentierte eigenständige
  Neubewertung ersetzt. Debuggings Verweise auf andere Skills werden durch kurze
  lokale Handlungsanweisungen ersetzt. Keine weiteren Skills nachladen.
  Hypothesen-/Testpflichten bleiben erhalten, technisch unmögliche Prüfungen müssen
  als solche dokumentiert werden. Begleitdateien mit beschreibenden Beispielen
  menschlicher Rückmeldungen bleiben unverändert; daraus folgt keine Rückfragepflicht.
- Keine Modell-Zeitgrenze und kein zusätzliches Tokenbudget. Der unveränderte
  offizielle Evaluator behält seine Grenze von 3.600 Sekunden.
- Externe Recherche wird wie bisher über Container-Netzwerk/Allowlist verhindert;
  nur Modell-/Authentifizierungshosts sind erlaubt. Native Unteragenten sind
  deaktiviert. Keine Änderungen am gemeinsamen `run.py` oder Evaluator.
- Maximal fünf gleichzeitige gesamte Versuche, standardmäßig fünf. Je Container
  weiterhin vier CPUs/8 GiB; fünf Worker sind kein Versprechen über tatsächlichen
  RAM-Verbrauch. Mindestens 25 GiB Speicherreserve auf Linux und Windows werden
  über den bestehenden Guard geprüft. Keine automatische Image-Löschung.
- Aufgabenblöcke 1–100, 101–200, 201–300. Innerhalb jeder Aufgabe wird die
  Variantenreihenfolge vorab reproduzierbar randomisiert, Seed 20261026.
  Der FIFO-Workerpool startet Jobs in der geplanten Reihenfolge; ihre Fertigstellung
  und erste tatsächliche Modellantwort können wegen unterschiedlicher Vorbereitung
  abweichen. Es ist keine Zusage exakt gleichzeitiger Modellstarts.
- Quelltexte, Skills, Auswahl, Dataset, Evaluatorskripte und Codex-Binärdateien werden
  bei `prepare` gehasht. Änderungen blockieren neue Modellstarts. Laufende historische
  Experimente und globale Codex-Skills werden nicht verändert.

## Kontrollen und Unterbrechungen

Kontrollen werden einmal gemeinsam pro Aufgabe verwendet. Der bestehende
`control_reuse.py` importiert nur passende Kontrollen bei exakten Quellen-, Daten-,
Aufgaben-, Evaluator- und Image-Prüfungen. Fehlende Kontrollen/Snapshots werden durch
den unveränderten `run.py` vorbereitet und validiert. Das darf offizielle Images und
Abhängigkeiten im vertrauenswürdigen Vorbereitungsschritt herunterladen; Agenten
und offizielle Tests bleiben offline. Gold-Patches werden niemals in Modellcontainer
oder Skill-Anweisungen übernommen.

`controls` startet **keine Modelle**. Ein fehlgeschlagener neuer Kontrolllauf bleibt
erhalten. Die zehn bereits beschlossenen Ausschlüsse werden nur angewendet, wenn
ein fehlgeschlagener Kontrollnachweis vorhanden ist. Neu scheiternde Aufgaben
werden nicht automatisch ausgeschlossen. Wenn bekannte Ausschlüsse erstmals lokal
bestätigt wurden, `controls --repair-controls` verwenden, um sie explizit zu übernehmen.
Bei anderen Fehlern zuerst Ursache prüfen. `prepare` verlangt einen vollständig
validierten Kontrollblock und vorhandene Images; es lädt oder baut selbst keine Images.

Technische Modellunterbrechungen werden bei ausdrücklichem `resume` archiviert und
mit frischem Kontext wiederholt. Regulär abgeschlossene falsche, leere und ungültige
Einreichungen bleiben Ergebnisse, unabhängig vom Score. Ein bloß gescheiterter
Evaluator wird mit dem unveränderten Patch wiederholt, ohne neuen Modellaufruf.
Ein abgeschlossener Modellschritt ohne exportierbare Einreichung verlangt Prüfung,
statt stillschweigend einen zweiten Modellversuch zu erzeugen. Alle Anläufe bleiben
erhalten; der Bericht weist bekannten zusätzlichen Tokenverbrauch separat aus.

## Startbefehle

Im Laborordner, zuerst **nur Block 01**:

```bash
bash run_skills_batch.sh 01 controls
bash run_skills_batch.sh 01 prepare
bash run_skills_batch.sh 01 check
bash run_skills_batch.sh 01 models
```

Jeder Befehl ist ein eigener Schritt. Erst nach erfolgreichen Kontrollen vorbereiten
und erst nach erfolgreicher Vorbereitung Modelle starten. Bei bekannten gescheiterten
Kontrollen oder einer geprüften technischen Kontrollunterbrechung:

```bash
bash run_skills_batch.sh 01 controls --repair-controls
```

Nach einer technischen Modellunterbrechung oder Pause:

```bash
bash run_skills_batch.sh 01 resume
```

Aktive Versuche fertigstellen lassen und danach pausieren (zweites Terminal):

```bash
bash run_skills_batch.sh 01 stop
```

Gesammelten Bericht aller bisher vorbereiteten Blöcke erzeugen:

```bash
.venv/bin/python run_skills.py report
```

Danach die vier Startbefehle mit **02** beziehungsweise **03** wiederholen.
Keine automatische Schleife startet die nächsten Blöcke oder löscht Images.
Weniger Worker können bei der Vorbereitung festgelegt werden, müssen anschließend
bei `models`, `check` und `resume` identisch angegeben werden, beispielsweise
`--model-workers 2`. Kontrollparallelität separat mit `--control-workers N` ändern;
bei eingefrorener Kontrollpolicy zuerst prüfen und explizit reparieren.

## Ordner

```text
skills-study/                         eingefrorene Originale, Anpassungen, Diffs
experiment-skills-sol6-medium-controls/
  batch-01/                          gemeinsame Kontrollnachweise und Snapshots
  batch-02/
  batch-03/
experiment-skills-sol6-medium/
  experiment.json                    gemeinsame Studienregeln
  batch-01/
    manifest.json                    Aufgaben, Reihenfolge, Hashes, Status
    source-snapshot/                 eingefrorene Quellen ohne Zugangsdaten
    task-01/
      controls.json
      preparation/snapshot.json
      standard/                      frischer Standardversuch
      tdd/
      debugging/
      verification/
    technical-interruptions/         erhaltene frühere Anläufe
  batch-02/
  batch-03/
  report/summary.md                   gesammelter Bericht
  report/summary.json
  report/tasks.csv
```

Innerhalb jeder Variante bleiben unter `standard/` die unveränderten technischen
Lognamen des gemeinsamen Ein-Agenten-Runners erhalten. Beispiel:
`task-01/tdd/standard/events.jsonl` gehört zum TDD-Versuch, nicht zum Standardarm.
`submission.patch`, `result.json` und `evaluation/` stehen direkt im Variantenordner.

## Auswertung und Befolgung

Primärer Endpunkt ist die offizielle binäre Lösung. Drei vorab festgelegte gepaarte
Vergleiche gegen frischen Standard: exakter zweiseitiger McNemar-Test, Holm-Korrektur
der drei p-Werte. Gepaarter Aufgaben-Bootstrap mit 10.000 Ziehungen für den Unterschied
der Lösungsquoten, feste Seeds, unadjustierte 95%-Intervalle. Keine
Repository-Clusterkorrektur; Aufgaben desselben Projekts können abhängig sein.
Die Tests werden erst bei vollständigen vier Bedingungen auf allen 290 bewertbaren
Aufgaben ausgegeben. Zwischenberichte sind beschreibend; keine optionale Beendigung
aufgrund günstiger Zwischenergebnisse.

Sekundär: bekannte Tokens, Vollständigkeit der Nutzungserfassung, Modellprozesszeit,
Fehlerarten und Prozessbeobachtungen. Cache-Eingabe und Reasoning-Ausgabe werden
nicht doppelt gezählt. Fehlende Nutzung bleibt unbekannt. Kein API-Preis und keine
Umrechnung in Abo-Prozent. Hoher Aufwand kann neben höherer Lösungsquote stehen;
es gibt keinen erzwungenen Gesamtsieger.

`skill-loading.json` protokolliert die Textinjektion. `skill-observations.json`
sammelt erkannte Testbefehle, Ausgaben/Exitcodes, Red-Green-Kandidaten und explizite
Ursachen-/Umgebungsaussagen. Diese Heuristiken übersehen mögliche Code-Mode-Aktionen
und beweisen weder korrekte Testassertionen noch Test-First oder Ursachenanalyse.
Für eine belastbare Befolgungsauswertung ist eine manuelle Prüfung der vollständigen
Events, Änderungen und Checkpoints erforderlich; keine zusätzlichen Modell-Judge-Tokens.

Optional pro Versuch `skill-review.json` speichern:

```json
{
  "classification": "technically_blocked",
  "evidence": ["standard/events.jsonl: Ereignis 12: pytest scheitert an fehlender Abhängigkeit"],
  "notes": "Testpflicht technisch nicht erfüllbar; keine Aussage über Patch-Korrektheit"
}
```

Klassen: `complied`, `not_followed`, `technically_blocked`, `unclear`, `pending`.
Jede Bewertung außer pending benötigt Belegstellen. Für TDD die Reihenfolge von
Testanlage, erwartungsgemäßem Fehlschlag, Produktionsänderung und erfolgreichem Lauf
prüfen; für Debugging die belegte Hypothese vor Reparatur und Neubewertung bei
Misserfolg; für Verification frische passende Prüfung und durch sie gedeckte Aussagen.
Nichtbefolgung oder technische Blockade führen **nicht zum nachträglichen Ausschluss**.
Die primäre Auswertung bleibt nach zugeteilter Bedingung (Intention-to-treat).

Die Aufgaben sind bereits bekannt; Sol medium wurde anhand früherer Untersuchungen
gewählt. Die neue Reihe untersucht Zusatznutzen auf dem bekannten Aufgabensatz und
liefert keinen unabhängigen Generalisierungsnachweis auf unbekannten Aufgaben.
Ein Endversuch je Aufgabe und Bedingung erfasst zudem keine verlässliche
Streuungsverteilung wiederholter Modellantworten auf derselben Aufgabe.
