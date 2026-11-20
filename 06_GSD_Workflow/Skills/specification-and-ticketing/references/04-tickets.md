# Phase 4: Implementierbare Tickets

**Eingang:** Freigegebene Spezifikation und dokumentierte offene Punkte.
**Ausgang:** Kleine, rückverfolgbare Tickets mit sinnvollen Abhängigkeiten.

Nutze `assets/ticket.md`; vergebe IDs `T-001` usw. Bevorzuge schmale vertikale
Schnitte, deren Verhalten unabhängig demonstrier- oder prüfbar ist. Keine starre
Zerlegung nach Datenbank/API/UI, wenn dadurch kein Ticket allein verifizierbar wäre.
Bei großen mechanischen Migrationen sind begründete Expand–Migrate–Contract-Schritte
zulässig; breite Refactorings nicht ohne Scope-Bezug hinzufügen.

Jedes Ticket enthält Beschreibung, Spec-Revision, Anforderungs-/Kriterien-IDs,
Mockups/Bildbezüge, Abhängigkeiten, geplante Tests, Definition of Done und offene
Blocker. Tickets führen keine neue Fachlichkeit ein. Nicht gedeckte Wünsche zur
Klärung und nötigenfalls Spec-Änderung zurückgeben.

Prüfe Vollständigkeit und Doppellungen gegen die Spezifikation. Dokumentiere echte
Blocking-Kanten, vermeide Zyklen, und schlage eine Reihenfolge vor. Falls zwei
Tickets unabhängig sind, heißt das nicht, dass sie automatisch parallel von
Unteragenten implementiert werden dürfen.

Zeige dem Nutzer den Zuschnitt und berücksichtige Rückmeldung. Eine separate
pauschale Ticket-Freigabe ist kein zusätzlicher Pflichtkontrollpunkt; die konkrete
Ticketplan-Freigabe muss aber den beabsichtigten Zuschnitt abdecken.

Speichere lokal einen Eintrag je Ticket, Status zunächst `draft`. Wähle als
`next_ticket` ein Ticket mit erledigten Abhängigkeiten und ohne offenen fachlichen
Blocker. Ein als offen dokumentierter Punkt darf keine stillschweigende Annahme werden.

**Rückgabe:** Genau das nächste Ticket für Phase 5 benennen und an die zentrale
Steuerung übergeben. Keine automatische Tracker-Veröffentlichung oder Änderung
übergeordneter Issues.
