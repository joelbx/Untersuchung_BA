# Temporäre Prüfhilfe und verbindlicher Rückbau

## Im freizugebenden Plan festlegen

Wenn Akzeptanzkriterien sonst für den Menschen schwer zugänglich sind, z.B. ohne
GUI, plane eine kleine ausführbare Prüfhilfe für den echten Funktionspfad: CLI,
minimaler lokaler Prototyp oder kontrollierter Aufruf bestehender Schnittstellen.
Keine reine Attrappe als Funktionsnachweis. Keine zusätzliche Endnutzerfunktion.
Dokumentiere Zweck, genaue Dateien/Einstiegspunkte, Start-/Prüfschritte, erwartete
Ergebnisse und Grenzen. Vor Erstellung Spec-/Planfreigaben prüfen. Sichere Ausführung
nach Projektregeln; Tests mit externen Effekten nur im vereinbarten Testsystem.

Nimm die vollständige Entfernung als Akzeptanzkriterium und Definition of Done auf.
Erfasse in `temporary_test_aids` am Ticket jeden Eintrag nach der
[Vorlage](../assets/temporary-test-aid.json), einschließlich geplanter Routen,
Schalter, Abhängigkeiten und Konfiguration. Dauerhafte automatisierte Tests sind
keine temporäre Produktoberfläche und bleiben erhalten. Keine nicht genehmigte
Prüfhilfe still entfernen oder als neue Produktanforderung behalten.

## Prüf-/Rückbaupfad

1. Implementierungsagent baut die freigegebene Hilfe und protokolliert ihre tatsächlichen
   Bestandteile und Verwendung. Review-Agent prüft echte Funktion samt Hilfe.
2. Koordinator legt dem Nutzer ausführbare Prüfschritte und Ergebnisse vor. Warte
   auf seine tatsächliche Funktionsprüfung. Quelle und Aussage in `human_check`
   festhalten. Bei Problemen Nachbesserung, kein Rückbau vor brauchbarer Prüfung.
   Diese Aussage ersetzt nicht die endgültige Abnahme.
3. Ein **neuer Rückbau-Agent** liest Ticket, genehmigten Plan, Inventar und menschliche
   Prüfaussage. Er entfernt ausschließlich die temporären Bestandteile; erhält
   Produktverhalten und dauerhafte Tests. Inventar mit tatsächlichem Diff abgleichen,
   Start-/Build-Einbindungen, Routen, Schalter, Abhängigkeiten und Konfiguration prüfen.
   Ausgeführte Tests und tatsächlichen Endstand dokumentieren.
4. Ein **neuer Abschlussverifikations-Agent** prüft Entfernung und endgültigen Code,
   führt relevante Tests/Build/Regression aus und erstellt Review-/Rückbaubelege.
   `status: removed` erst bei nachgewiesenem Rückbau; `removal_evidence` und
   `verification_evidence` referenzieren versionierte Berichte mit Codeidentität.
   Ein bewusst eingerichteter Prüfhilfen-Schalter gilt nicht als Entfernung.
5. Neuer Agent bereitet abschließenden Abnahmebericht vor. Der Koordinator legt dem
   Menschen den **Stand nach Rückbau** vor. Erst ausdrückliche Endabnahme erlaubt `done`.

Rückbau ist durch den zuvor freigegebenen Plan gedeckt, kein neues Pflicht-Freigabegate.
Weicht er wesentlich davon ab, betroffene Planfreigabe erneuern. Misslingt eine
Prüfung, Ticket offen lassen; Rückbau oder Tests nicht als erfolgreich behaupten.

## Persistenz und Abschlusssperre

Ticketfeld `temporary_test_aids` ist bei neuen Tickets immer vorhanden: `[]`, wenn
keine Hilfe benötigt wird. Einträge: eindeutige `id`, `status` (`planned`, `present`,
`removed`), `inventory`, `human_check` mit echter `source` und `quote`,
`removal_evidence`, `verification_evidence`. Eine einst erstellte Hilfe nicht aus
der Liste löschen, um die Sperre zu umgehen. Historie als Ereignisse erhalten.
Prüfungsergebnis der menschlichen Prüfung zusätzlich im Bericht festhalten.

Der Abnahmebeleg muss auch die referenzierten Rückbau- und Verifikationsberichte
hashen. Ohne `removed`, menschliche Prüfaussage und beide Berichte darf `done`
nicht gesetzt werden. Der lesende Zustandsprüfer prüft diese gespeicherten
Voraussetzungen, aber weder tatsächliche Dateientfernung noch echte menschliche
Identität. Die Abschlussverifikation muss beides inhaltlich anhand der Belege prüfen.
