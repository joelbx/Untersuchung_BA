# Phase 6: Ticketweise Implementierung

**Eingang:** Gültige Spec-/Ticketplan-Freigaben, freies Ticket, vereinbarte Prüfgrenzen.
**Ausgang:** Implementierung mit nachvollziehbaren Prüfschritten.

Prüfe die Freigaben vor der ersten Änderung. Setze Ticket und aktives Feature auf
`implementing`. Verwende die vereinbarten Projektwerkzeuge und keine erfundenen
fachlichen Defaults.

## TDD für geeignetes Verhalten

1. Leite einen kleinen Verhaltenstest aus einem Akzeptanzkriterium ab. Beobachte
   öffentliche Schnittstellen; Erwartungen kommen aus Spec/Beispiel, nicht aus
   derselben Berechnung wie die Implementierung.
2. Schreibe den Test und führe ihn **vor** der Produktionsänderung aus. Sichere
   Befehl und relevanten Fehlschlag. Ein fehlender Test-Runner, Importfehler oder
   Syntaxfehler beweist noch keine fehlschlagende Verhaltensassertion. Behebe die
   Testvoraussetzung oder dokumentiere diesen schwächeren Red-Nachweis ausdrücklich.
3. Implementiere nur genug für dieses Verhalten, führe den Test erneut aus,
   analysiere Fehlschläge und korrigiere sie. Ein sofort grüner neuer Test belegt
   keinen Red-Green-Zyklus; prüfe, ob er tatsächlich das fehlende Verhalten erfasst.
4. Wiederhole vertikal: ein Verhalten → ein Test → minimale Implementierung.
   Nicht alle denkbaren Tests vorab gegen eine imaginierte Architektur schreiben.
5. Refaktoriere bei Bedarf innerhalb des freigegebenen Umfangs bei grünen Tests.
   Danach Checks erneut ausführen. Die Möglichkeit dieser Refactoring-Schritte
   ist hier bewusst weiter gefasst als im untersuchten Matt-Pocock-TDD-Skill.
6. Führe die vereinbarten relevanten Regressionstests aus. Dokumentiere den Umfang;
   keine pauschale Behauptung einer grünen Gesamtsuite aus einem Pakettest.

## Alternativen und Hindernisse

Bei rein visuellen oder anderweitig nicht sinnvoll automatisierbaren Änderungen
die im Plan vereinbarte Alternative anwenden: beispielsweise reproduzierbarer
Screenshot-/Mockup-Vergleich oder ein manueller nachvollziehbarer Prüfschritt.
Keine nutzlosen Tests nur zur Erfüllung einer Ritualvorgabe erzeugen.

Wird eine vereinbarte Prüfung technisch unmöglich, protokolliere Befehl, Fehler,
betroffene Kriterien und sichere Alternativen. Nicht als bestanden markieren.
Wenn dadurch eine wesentliche Planänderung oder fachliche Entscheidung nötig wird,
blockieren und zur passenden Phase zurückkehren. Begrenze erfolglose identische
Wiederholungen; neue Versuche brauchen neue Evidenz oder eine behobene Ursache.

Korrekturen innerhalb des freigegebenen Plans darf der Agent selbst durchführen.
Scope-Erweiterungen brauchen die entsprechende erneute Freigabe. Aktualisiere
Status, Belege und Korrekturschleifen; den Stand für Phase 7 an die zentrale
Steuerung zurückgeben, nicht selbst den nächsten Skill starten.
