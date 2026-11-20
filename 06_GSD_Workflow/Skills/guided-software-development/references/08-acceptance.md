# Phase 8: Menschliche Abnahme

**Eingang:** Aktueller Review-Stand mit Prüfbelegen und offengelegten Grenzen.
**Ausgang:** Ausdrückliche Abnahme oder konkrete Nachbesserungsanforderung.

Bereite den Bericht in einem neuen Kontext im Modus `acceptance_preparation` vor.
Du bist nur für diesen Bericht zuständig, startest keine weiteren Agenten und
erteilst keine Abnahme. Der Koordinator übermittelt die Frage an den Menschen.
Nutze `assets/acceptance.md`. Fasse umgesetzte Anforderungen, geänderte Komponenten,
Tests/Build/Regression, visuelle Prüfung, Abweichungen, Einschränkungen und offene
Punkte verständlich zusammen. Verlinke Nachweise, statt Erfolg pauschal zu behaupten.
Kennzeichne ungeprüfte Akzeptanzkriterien separat von nachgewiesenen Fehlern.

Prüfe bei temporären Prüfhilfen zuerst die [Rückbauregeln](temporary-test-aids.md).
Ohne dokumentierte menschliche Funktionsprüfung, vollständige Entfernung und frische
Abschlussverifikation keine endgültige Abnahme anfordern. Eine Bestätigung der
Funktion vor Rückbau nicht als Endabnahme verwenden.

Halte Ticket-, Spec-, Plan-, Review-Revision und bewertete Codebasis fest. Frage
explizit, ob der Mensch **dieses Ticket in diesem Stand** annimmt oder Änderungen
fordert. Warte auf seine Antwort. Ein Reviewer, ein Unteragent oder ein Testlauf
kann diese Entscheidung nicht treffen.

Bei Abnahme: ehrliche Nutzerentscheidung mit Umfang/Belegen in `approvals.jsonl`
speichern; Rückbau-/Verifikationsberichte im Beleg ebenfalls hashen. `acceptance_approval` verknüpfen und erst dann Ticket `done` setzen.
Ausdrücklich akzeptierte Einschränkungen nicht in bestandene Tests umdeuten;
eine akzeptierte Lieferung kann weiterhin dokumentierte Prüflücken enthalten.
Geforderte fachliche Kriterien dürfen nicht stillschweigend abgeschwächt werden;
eine echte Anforderungsänderung braucht die entsprechende Spec-/Planrevision.

Bei Nachbesserung: Anforderungen dokumentieren, Korrekturschleife zählen. Innerhalb
des gültigen Plans mit frischem Implementierungsagenten zu `implementing` zurück; bei geändertem Umfang zur Klärung/
Spec-/Planfreigabe. Nach Änderungen Review aktualisieren und erneut abnehmen lassen.

Bei ausbleibender oder unklarer Antwort bei `acceptance` bleiben. Vor Pause den
Stand und die konkrete offene Abnahmefrage speichern. Danach nächstes freies Ticket
bestimmen; Feature erst bei vollständigen Ticketabnahmen und Dokumentation `done`.
