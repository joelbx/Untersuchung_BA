# Koordinator: Phasen- und Ticketschleife

## Kontextvertrag

Der Koordinator hält Feature-Zustand, Reihenfolge, Gates und Messwerte. Er delegiert
jede fachliche Entwicklungsphase an genau einen neuen Worker ohne geerbten Chat.
Bei der hier vorhandenen `collaboration.spawn_agent`-Schnittstelle ist dafür
`fork_turns: "none"` nötig. Andere Laufzeiten benötigen einen belegbaren äquivalenten
Mechanismus. Keine API-Schlüssel, Anbieterwechsel oder globale Konfigurationsänderung.
Neue Prompts, Skillwechsel und Kompaktierung erzeugen keinen frischen Kontext.

Frisch heißt ohne vorherigen Gesprächsverlauf/Agentenreasoning. Systemregeln,
Werkzeuge, Projektregeln, genehmigte Artefakte und die aktuelle Codebasis sind
weiter verfügbar. Threads trennen nicht Dateisystem oder Berechtigungen. Bereits
abgenommene Änderungen bleiben sichtbar. Kein Anspruch auf hermetische Isolation.

## Eine Phase ausführen

1. Bestimme die nächste erlaubte Phase anhand von Zustand, Artefakten und tatsächlichen
   Freigaben. Speichere `execution.phase`, das aktive Ticket oder `null` für Feature-
   Phasen sowie die nächste Aktion. Freigaben sind kein Ersatz für fehlende Inhalte.
2. Finalisiere `handoffs/<scope>-<phase>-<attempt>.json` aus der
   [Vorlage](../assets/phase-agent-handoff.json). Übergib Projekt-/Feature-Wurzeln,
   genau einen Phasenauftrag, Artefaktpfade mit SHA-256 und Zweck, Gate-IDs, bekannte
   Blocker und erwartete Ausgaben. Übergib keine früheren Chats oder pauschalen
   Gesprächszusammenfassungen. Relevante Ergebnisse stehen in versionierten Artefakten.
3. Starte den Worker ohne Gesprächsvererbung mit Übergabepfad und passendem Skill/Modus
   aus der Tabelle unten. Er liest echte Quellen und Freigabebelege. Übergib diesen
   engen Auftrag: **nur die genannte Phase; keine eigenen Folgeagenten oder Schleife**.
   Erfasse tatsächlichen Start, Agent-/Thread-ID und Kontextnachweis. Niemals dieselbe
   Agent-/Thread-ID für unterschiedliche Phasen wiederverwenden.
4. Innerhalb dieser Phase bleibt derselbe Worker aktiv, auch bei Rückfragen und
   Iterationen. Kann er nicht direkt mit dem Nutzer sprechen, liefert er genau eine
   Frage samt Empfehlung und Frage-ID an den Koordinator. Dieser fragt und wartet;
   nur echte Antwort/Quelle wird zurückgereicht. Keine stellvertretende Entscheidung.
5. Lass den Worker Ergebnisse, Evidenz, offene Fragen und Messdaten dauerhaft speichern.
   Prüfe Rückgaben und Freigabegültigkeit. Beende/freigebe den Worker nach Laufzeit-
   möglichkeit; bevor ein anderer schreibender Worker beginnt, muss der vorige sicher
   inaktiv sein. Nächste Phase immer mit neuem Kontext. Kein bloßes „Rolle wechseln“.

## Phasenfolge

| Phase-ID | Ausführung / Ergebnis |
|---|---|
| `intake` | requirements-clarification / intake: Quellen und Projektgrenzen |
| `requirements_clarification` | requirements-clarification / clarification: dokumentierte Entscheidungen |
| `specification` | specification-and-ticketing / specification: Spec zur menschlichen Freigabe |
| `ticketing` | Nach echter Spec-Freigabe: specification-and-ticketing / tickets |
| `ticket_clarification` | requirements-clarification / ticket: offene Umsetzungsentscheidungen; keine künstlichen Fragen |
| `planning` | ticket-planning: Plan aus gespeicherten Klärungsergebnissen; menschliche Freigabe |
| `implementation` | ticket-implementation: TDD samt Red/Green/Refactor in einem Kontext |
| `review` | verification-and-review: frisch prüfen, innerhalb des Plans korrigieren und nachtesten |
| `cleanup` | Nur bei Prüfhilfe und nach menschlicher Funktionsprüfung: Rückbau nach Prüfhilfenreferenz |
| `final_verification` | Nach Rückbau: neuer verification-and-review-Agent prüft Produktstand und Rückbau |
| `acceptance_preparation` | Neuer Worker liest Abnahmeregel und bereitet endgültigen Abnahmebericht vor; Mensch entscheidet |

Der Koordinator übermittelt Freigabe-/Abnahmefragen anhand der vorbereiteten
Artefakte und wartet auf die tatsächliche Entscheidung. Diese Kommunikation,
Zustandsführung und begleitende Messung brauchen keinen zusätzlichen Agenten pro
Nachricht. Ein Agent kann niemals menschliche Abnahme erteilen.

## Ticketfolge und Rücksprünge

Nach der Ticketzerlegung wähle das erste unerledigte Ticket in dokumentierter
Reihenfolge mit vollständig abgenommenen Abhängigkeiten. Blocker nicht still
überspringen; Reihenfolgeänderung mit dem Nutzer klären. Nur ein Ticket aktiv.
Durchlaufe dessen Klärung, Planung und freigegebene Umsetzung bis zur Endabnahme.
Bei Prüfhilfe nutze zusätzlich den [Prüf-/Rückbaupfad](temporary-test-aids.md).

Lehnt der Mensch die Abnahme ab, dokumentiere Korrekturen und starte die nötige
Umsetzungsphase frisch, danach einen neuen Review-Agenten und neue Abnahmevorbereitung.
Der Reviewer darf während seiner Phase selbst korrigieren; seine Änderungen sind
anschließend Selbstreview, nicht durch einen weiteren unabhängigen Reviewer bestätigt.
Bei neuen fachlichen Entscheidungen zur Klärung, bei wesentlichem Plan-/Scopewechsel
zu den betroffenen Freigaben zurück. Kein automatisches Verwerfen gültiger Belege.
Erst nach endgültiger menschlicher Abnahme `done`; dann nächstes Ticket frisch.
Sind alle Tickets abgenommen, tatsächlichen Abschlussbericht und Messdaten sichern.

## Wiederaufnahme und Nachweis

Speichere Phase, aktiven Versuch, offene Frage/Gate und nächste Aktion vor dem Warten.
Ein vorhandener Worker darf nur innerhalb exakt derselben Phase desselben Tickets
weiterverwendet werden. Ist er verloren oder die Phase beendet, neuer Versuch mit
frischem Kontext und gespeicherten Artefakten. Alte Versuche/Codeänderungen behalten;
keine automatischen Resets. Bei fehlender Kontextfunktion `fresh_context_unavailable`
als Blocker speichern und einen neuen Chat mit Übergabe anfordern.

`phase_agent_attempts` enthält Phase, Scope/Ticket, Versuch-/Agent-/Thread-IDs,
Kontextmodus/-quelle, Übergabepfad/-Hash, Zeiten und Status. Unbekanntes bleibt
`null` mit Grund. Tatsächlich gestartete Agenten von vorbereiteten Übergaben trennen.
Fragenweiterleitungen nicht doppelt zählen. Koordinator-, Worker-, Warte-, Rückbau-
und Wiederholungsaufwand getrennt erfassen. Strukturprüfungen können gespeicherte
Widersprüche erkennen, aber den realen Kontextwechsel nicht beweisen.
