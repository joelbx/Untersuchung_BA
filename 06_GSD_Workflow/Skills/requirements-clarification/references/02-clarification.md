# Phase 2: Strukturierte Anforderungsklärung

**Eingang:** Quelleninventar, Projektanalyse, bekannte Unklarheiten.
**Ausgang:** Beantwortete Entscheidungen und explizit eingegrenzte offene Punkte.

Führe eine kleine Entscheidungslandkarte: Frage-ID, Thema, Abhängigkeiten,
vorhandene Belege, Antwort/Entscheidung, Auswirkungen und Status. Frage nur an der
aktuellen Entscheidungsfront: keine Detailfrage, deren Voraussetzungen ungeklärt sind.

Prüfe gezielt:
- widersprüchliche oder fehlende Anforderungen und Mockup-Abweichungen;
- Akteure, Rechte, Eingaben, Zustände, Randfälle und fachliche Regeln;
- Fehlerbehandlung und Wiederholbarkeit/Seiteneffekte, soweit fachlich relevant;
- Architekturgrenzen, Schnittstellen und technische Restriktionen;
- beobachtbare Akzeptanzkriterien und geeignete Prüfgrenzen.

Stelle standardmäßig **eine Frage nach der anderen**. Formuliere sie konkret,
nenne nachvollziehbare Optionen und eine begründete Empfehlung. Die Empfehlung ist
keine Entscheidung. Vor mehreren Fragen gemeinsam zunächst die Präferenz beachten.
Erfrage keine Fakten erneut, die aktuelle, eindeutige Projektartefakte beantworten.
Bei Widersprüchen Quellen nennen und gezielt die offene Entscheidung erfragen.

Übernimm Antworten zeitnah in `decisions.md`: echte Aussage, Ergebnis, betroffene
Anforderungs-/Mockup-IDs, verbleibende Unsicherheit. Ein hypothetischer Randfall
ist ein Prüfangebot an den Menschen, keine automatisch neue Anforderung.
Verwende die vorhandene Fachsprache; definiere nötige Begriffe im Projektglossar,
ohne Glossar und Spezifikation zu vermischen. ADRs nur bei echten, dauerhaften
Architekturentscheidungen mit Alternativen, nicht für jede Implementierungsnotiz.

Die Phase endet, wenn wesentliche Entscheidungen geklärt oder ausdrücklich offen
dokumentiert sind. Benenne für jeden offenen Punkt, welche Tickets er blockiert.
Ein Nutzer kann einen Punkt bewusst verschieben; das ist keine Erlaubnis, seine
fachliche Antwort bei der Implementierung zu erfinden.

**Rückgabe:** Phase 3 als nächsten Schritt benennen, nicht selbst starten.
Offene, implementierungsrelevante
Entscheidungen bleiben auch bei einer Spec-Freigabe für betroffene Tickets blockierend.
