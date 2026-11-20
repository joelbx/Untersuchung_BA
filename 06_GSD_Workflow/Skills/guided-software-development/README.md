# guided-software-development

Ein wiederverwendbarer Mensch-KI-Workflow mit drei verbindlichen Kontrollpunkten:
**Spec-Freigabe → Ticketplan-Freigabe → menschliche Ticketabnahme**.
Anforderungen und Mockups werden in nachvollziehbare Tickets, Codeänderungen,
Prüfbelege und Messprotokolle überführt. Bundle-Version **1.3.0** enthält einen
Oberskill und fünf Unter-Skills. Es wurde kein Anwendungsfeature implementiert
oder Projektworkflow gestartet.

## Aufteilung und Progressive Disclosure

| Skill | Aufgabe |
|---|---|
| `guided-software-development` | Routing, Zustand, gemeinsame Regeln, Freigaben, Abnahme und Evaluation |
| `requirements-clarification` | Aufnahme und Klärung, jeweils als eigener Modus |
| `specification-and-ticketing` | Spec erstellen oder nach Freigabe Tickets ableiten |
| `ticket-planning` | Konkreten Ticketplan erarbeiten und zur Freigabe vorlegen |
| `ticket-implementation` | Genau ein gültig freigegebenes Ticket umsetzen |
| `verification-and-review` | Tatsächliche Änderungen verifizieren und strukturiert reviewen |

Progressive Disclosure: Codex sieht zunächst Name/Beschreibung; nur der ausgewählte
Skill und anschließend seine aktuell benötigte Referenz werden vollständig geladen.
Der Oberskill lädt nicht alle Unter-Skills vorab. Es handelt sich um Anweisungsrouting,
nicht um Funktionsaufrufe. Zusätzlich erzeugt die Ticketschleife ausdrücklich
frische Phasenagenten; diese Funktion muss die jeweilige Codex-Laufzeit anbieten. Ein spezielles
Skill-Tool ist nicht nötig: verfügbare Aktivierung oder Lesen der verlinkten SKILL.md.

Die fünf Unter-Skills sind auch direkt verwendbar, benötigen aber den gemeinsamen
Kern als Geschwisterordner. Sie lesen dieselben Regeln und gespeicherten Gate-Belege.
Kein Unter-Skill pflegt einen zweiten Zustand oder erteilt selbst menschliche Abnahme.
Die zusätzliche Modularität garantiert weder Tokenersparnis noch bessere Ergebnisse;
auch die fünf zusätzlichen Beschreibungen gehören zum Discovery-Kontext.

## Installation und Aktivierung in Codex

Alle sechs Ordner liegen bereits nebeneinander unter:

```text
~/.agents/skills/guided-software-development/
~/.agents/skills/requirements-clarification/
~/.agents/skills/specification-and-ticketing/
~/.agents/skills/ticket-planning/
~/.agents/skills/ticket-implementation/
~/.agents/skills/verification-and-review/
```

Codex dokumentiert `~/.agents/skills` für benutzerweite und `.agents/skills` für
Repository-Skills. Bei Wiederverwendung **alle sechs Ordner** mit ihren Ressourcen
kopieren, nicht nur die Hauptdateien. Relative Querverweise setzen diese Anordnung
voraus. Für eine geteilte, versionierbare Projektinstallation beispielsweise:

```bash
(
  set -e
  names=(guided-software-development requirements-clarification specification-and-ticketing
         ticket-planning ticket-implementation verification-and-review)
  for name in "${names[@]}"; do
    if [[ -e ".agents/skills/$name" || -L ".agents/skills/$name" ]]; then
      printf 'Ziel existiert bereits: %s\n' "$name" >&2
      exit 1
    fi
  done
  mkdir -p .agents/skills
  for name in "${names[@]}"; do
    cp -R "$HOME/.agents/skills/$name" .agents/skills/
  done
)
```

Nur kopieren, wenn das Ziel noch nicht existiert. Nicht gleichzeitig zwei aktive
Installationen desselben Namens verwenden; Codex kann beide im Selektor anzeigen.
Die benutzerweite Installation genügt für lokale Nutzung. Bundle-/Komponentenversionen
und Hashes für die Untersuchung festhalten. Die frühere einzelne Version 1.0.0 ist
unter `~/.agents/skill-archives/guided-software-development-1.0.0.tar.gz` archiviert,
außerhalb der Skill-Erkennung. Vorhandene Workflow-Artefakte und Freigaben bleiben
verwendbar; einen Versionswechsel während eines Features als Abweichung erfassen.

Im gewünschten Projekt Codex starten und `$guided-software-development` nennen.
Bei fehlender Anzeige mit `/skills` prüfen bzw. Codex neu starten. Die automatische
Auswahl anhand der Beschreibung bleibt erlaubt, ersetzt aber keine Freigabe.
Dokumentation: [Codex-Skills](https://learn.chatgpt.com/docs/build-skills).

## Startbeispiel mit Anforderungen und Mockups

```text
$guided-software-development

Begleite die Entwicklung des Features „[Feature]“ im aktuellen Projekt.
Anforderungen: [Pfad zur Anforderungsdatei]
Mockups: [Bildpfade oder erreichbare URLs mit den relevanten Zuständen]
Rahmenbedingungen: [vorhandene Dokumente oder konkrete Vorgaben]

Nutze die vorhandenen Repository- und Dokumentationskonventionen.
Beginne mit Aufnahme und Klärung. Stelle Fragen einzeln nacheinander.
Erstelle danach eine dauerhafte Spezifikation und lege sie zur Freigabe vor.
Implementiere erst nach Spec- und konkreter Ticketplan-Freigabe.
```

Hierdurch entstehen später **im Zielprojekt** die Feature-Artefakte, nicht im
installierten Skillordner. Standard: `docs/guided-development/<feature-id>/`;
vorhandene Projektkonventionen haben Vorrang. Nach Sitzungswechsel:

```text
$guided-software-development
Setze das Feature anhand von [Pfad zum Feature-Artefaktordner]/workflow.json fort.
Prüfe zuerst die gespeicherten Freigaben und benenne den nächsten erlaubten Schritt.
```

## Phasenschleife und Kontexttrennung

Ein Koordinator steuert jeweils einen frischen Agenten pro Phase. Dies gilt für
Aufnahme, Anforderungsklärung, Spec und Ticketzerlegung sowie innerhalb jedes Tickets:

**Ticketklärung → Planung → menschliche Planfreigabe → TDD-Implementierung →
Verifikation/Review → Abnahmevorbereitung → menschliche Abnahme → nächstes Ticket.**

Jeder Pfeil zwischen Agentenphasen bedeutet einen neuen Kontext ohne bisherigen
Chatverlauf. Innerhalb einer Phase bleiben Agent und Kontext während Rückfragen und
Iterationen erhalten; Red/Green/Refactor bilden gemeinsam eine Implementierungsphase.
Der Reviewer darf im Planumfang selbst korrigieren, kennzeichnet eigene Änderungen
als Selbstreview und testet erneut. Der Koordinator behält Zustand und übermittelt
menschliche Fragen/Freigaben. Ohne Antwort wartet die Schleife.

Kann die Funktion sonst schwer erprobt werden, etwa ohne GUI, wird im Plan eine
kleine temporäre Prüfhilfe genehmigt. Nach Review prüfst du damit die Funktion.
Dann folgen **frischer Rückbau-Agent → frische Abschlussverifikation → frische
Abnahmevorbereitung → deine endgültige Abnahme**. Die Prüfhilfe darf nicht im
fertigen Produkt bleiben; Inventar und Nachweise sperren `done`, solange sie offen ist.
Dauerhafte automatisierte Tests bleiben erhalten.

Ein Worker darf keine vorherige Unterhaltung erben. Die hier vorhandene Funktion
`collaboration.spawn_agent` verwendet dafür `fork_turns: "none"`; in anderen
Laufzeiten die reale Entsprechung prüfen. Bei fehlender Funktion wartet der Skill
mit gespeicherter Übergabe auf einen neuen Chat. Skillwechsel und Kompaktierung
sind kein Ersatz. Projektdateien und genehmigte Artefakte bleiben sichtbar;
Dateisystem und Berechtigungen sind dadurch nicht getrennt. Keine automatische
Codex-Konfigurationsänderung und keine zusätzlichen API-Aufrufe aus einem Skript.

Der `grill-me`-Wrapper verweist auf `grilling`. Der Ticket-Klärungsagent verwendet
dessen geprüftes Entscheidungsbaum-Prinzip, angepasst auf Einzelfragen und eigene
Faktenrecherche. Keine künstlichen Fragen bei eindeutigen Artefakten. Planung beginnt
anschließend in einem anderen Kontext. Ohne externen Skill greifen die eigenen
vollständigen Anweisungen; die tatsächlich verwendeten Skills werden protokolliert.

Details: [Phasenschleife](references/ticket-loop.md),
[Übergabe](assets/phase-agent-handoff.json),
[temporäre Prüfhilfen](references/temporary-test-aids.md).
Codex beschreibt [Subagenten](https://learn.chatgpt.com/docs/agent-configuration/subagents);
die konkreten Werkzeuge sind in der ausführenden Sitzung zu prüfen. Das Bundle sind
Agentenanweisungen und Vorlagen, kein separat gestarteter Hintergrunddienst.

## Nutzung und Projektanpassung

- Die Referenzen werden phasenweise geladen; Vorlagen bedarfsweise in den
  Feature-Artefaktordner kopieren und ausfüllen.
- Im Workflow-Zustand Projektwurzeln, Artefaktpfade, Revisionen, Status und Ticket-
  Beziehungen pflegen. Freigegebene Artefakte nicht überschreiben.
- Spec-, Plan- und Abnahmebelege als **je ein JSON-Objekt pro Zeile** in
  `approvals.jsonl` speichern. Die Vorlagendatei ist ein Schema, keine erteilte Freigabe.
- Modell/Reasoning, Prüfwerkzeuge, Dokumentationsort, Mockup-Versionen und
  Messquellen werden projektspezifisch angegeben. Keine Projekt-, Framework- oder
  Rechnungsregeln sind vorgegeben. Menschliche aktive Zeit braucht echten Timer
  oder Selbstbericht; fehlende Nutzungsdaten bleiben unbekannt.
- Standard ist ein Koordinator mit einem frischen Phasenagenten zur Zeit. Die
  fünf Unter-Skills sind Komponenten, keine fünf gleichzeitig aktiven Agenten.
  Nur tatsächlich geladene Komponenten als verwendet protokollieren.
- Alte laufende Features nicht still auf Kontexttrennung umdeklarieren: ab der
  nächsten Phase Bundle-Version und Ausführungsmodus dokumentieren. Bestehende
  gültige Freigaben behalten; offene Tickets auf temporäre Prüfhilfen prüfen.

Minimaler Ticket-Eintrag in `workflow.json` beim Anlegen eines Plans
(IDs/Bezüge durch echte Projektwerte ersetzen):

```json
{
  "id": "T-001",
  "status": "planned",
  "spec_revision": "S1",
  "plan_revision": "P1",
  "acceptance_revision": null,
  "spec_approval": "APP-S1",
  "plan_approval": null,
  "acceptance_approval": null,
  "depends_on": [],
  "temporary_test_aids": [],
  "artifacts": {
    "specification": "specifications/S1.md",
    "ticket": "tickets/T-001-T1.md",
    "plan": "plans/T-001-P1.md",
    "review": "reviews/T-001-R1.md",
    "acceptance": "acceptance/T-001-A1.md"
  }
}
```

## Validierung und Grenzen

```bash
python3 ~/.agents/skills/guided-software-development/scripts/check_workflow.py PFAD_ZUM_FEATURE_ORDNER
python3 -m unittest discover -s ~/.agents/skills/guided-software-development/tests -v
```

Der Zustandsprüfer liest nur. Er überprüft Struktur, Abhängigkeiten und gespeicherte
Gate-Belege einschließlich Hashes. Er prüft zusätzlich Rückbaubelege inventarisierter Prüfhilfen vor `done`.
Er kann weder echte menschliche Zustimmung
authentifizieren noch Kriterienerfüllung, Codebasis oder ausgeführte Tests beweisen.
Die Fixture-Tests prüfen diese mechanischen Regeln, nicht die Wirksamkeit des
Skills bei echter Softwareentwicklung. Ein kurzer begleiteter Pilot im Zielprojekt
bleibt vor der wissenschaftlichen Erhebung sinnvoll.

Die lokale Struktur wurde zusätzlich mit dem vorhandenen `skill-creator`-Validator
und Prüfungen von Dateiverweisen, Frontmatter und JSON-Vorlagen validiert.
`skills-ref` ist in dieser Umgebung nicht installiert; eine Ausführung dieses
Referenzvalidators wird nicht behauptet. Formatquelle:
[Agent Skills Specification](https://agentskills.io/specification).

Herkunft und Anpassungen: [Quellenvergleich](references/sources.md).
