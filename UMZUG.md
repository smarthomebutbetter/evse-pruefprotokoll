# Umzug auf das Firmenkonto – Ablauf

Stand 15.10.2026 · erstellt von M. Pevec

## 1. Vorher mit EDV Achenbach klären (ein Termin)

| Frage | Optionen |
|---|---|
| Wo sollen die Apps liegen? | **A** GitHub-Firmenkonto (kostenlos, Code öffentlich) · **B** Azure Static Web Apps (Microsoft, EU-Rechenzentrum, Anmeldung vor dem Laden möglich, für „nur Firmenkonten“ vermutlich Standard-Tarif ca. 9 $/Monat) · **C** Webspace beim Anbieter von elektro-irrgang.de |
| Eigene Adressen | **eine Subdomain pro App** (Empfehlung von Google, Android installiert sonst nicht zuverlässig mehrere Apps): `apps.`, `evse.`, `baustelle.`, `echeck.elektro-irrgang.de` – je ein DNS-Eintrag. Erst zusammen mit der Microsoft-Anbindung umstellen, weil die Apps dann keinen gemeinsamen Gerätespeicher mehr haben. |
| Microsoft-Registrierung | **eine** Registrierung „Elektro Irrgang Apps“ für alle Apps, Umleitungsadressen siehe `EINRICHTUNG-MICROSOFT.md` |
| Rechte | `User.Read`, `Files.ReadWrite.All` (gemeinsamer Ordner `_App-Daten` und persönliche Notizen im eigenen OneDrive), optional `Mail.Send` |
| Benutzerverwaltung | J. Irrgang bekommt die Rolle **Benutzeradministrator** in Microsoft 365 und legt Konten selbst an. Kein `User.ReadWrite.All` für die Apps. |
| Datenschutz | Datenschutzerklärung (Entwurf in EVSE unter Mehr → Datenschutz) prüfen, Hosting-Anbieter ergänzen |

Erst wenn Hosting und Adresse feststehen, trägt Achenbach die Umleitungsadressen ein – sonst muss er zweimal ran.

## 2. GitHub-Firmenkonto (falls Option A)

1. Mit `info@elektro-irrgang.de` eine **Organisation** auf github.com anlegen (z. B. `elektro-irrgang`), kostenloser Plan.
2. Eigentümer: J. Irrgang. **M. Pevec als Mitglied mit Rolle „Owner“ oder „Maintainer“** einladen. Optional Achenbach.
3. Repository **übertragen statt neu hochladen**: Settings → Danger Zone → *Transfer ownership* → Organisation wählen.
   Dadurch bleiben alle Commits, die Versionsgeschichte und die Mitwirkenden erhalten – M. Pevec steht dauerhaft als Mitwirkender im Repository.
4. In der Organisation: Settings → Pages → ggf. eigene Adresse eintragen und „Enforce HTTPS“ aktivieren.
5. In `README.md` steht: Entwickelt von M. Pevec für Elektro Irrgang.

### Aufbau der Repositories – zwei Möglichkeiten

| | Ein Repository für alle Apps (wie jetzt) | Ein Repository pro App |
|---|---|---|
| Gemeinsamer Code (Anmeldung, Kunden, Design) | einmal vorhanden | in jedem Repository kopiert |
| Neue Version | ein Build, alle Apps gleich aktuell | jede App einzeln |
| Übersicht für Außenstehende | alles an einem Ort | sauber getrennt |
| Gemeinsamer Speicher im Browser | ja | ja (gleiche Adresse `…github.io`) |

Empfehlung als Input: vorerst **ein** Repository `apps` behalten und bei Bedarf später aufteilen.

## 3. Daten mitnehmen (wichtig)

Eine neue Adresse bedeutet für den Browser einen leeren Speicher.

1. **Vor dem Umzug** in jeder App auf jedem Gerät: Mehr → **Alle sichern** (EVSE, Baustellenübergabe).
2. Nach dem Umzug: neue Adresse öffnen, Apps einzeln zum Home-Bildschirm hinzufügen, alte Symbole löschen.
3. In jeder App: Mehr → **Sicherung laden**.
4. Mit der Microsoft-Anbindung entfällt das künftig – dann liegen die Daten im Firmenordner.

## 4. Nach dem Umzug prüfen

- [ ] Startseite, `/evse/`, `/baustelle/` öffnen sich
- [ ] Anmeldung funktioniert
- [ ] Sicherungen eingespielt, Kunden und Prüfungen vollständig
- [ ] PDF erstellen und per Mail senden klappt
- [ ] Alte Adresse `smarthomebutbetter.github.io/evse-pruefprotokoll/` leitet um oder zeigt einen Hinweis
