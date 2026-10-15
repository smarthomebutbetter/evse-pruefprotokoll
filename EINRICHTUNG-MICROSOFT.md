# EVSE-Prüfprotokoll – Anbindung an Microsoft 365

Die App ist eine Web-App (eine HTML-Datei, läuft offline auf den iPads). Damit die Prüfprotokolle aller Mitarbeiter in einem gemeinsamen Ordner der Firma landen, meldet sich jeder Nutzer einmal mit seinem Microsoft-Mitarbeiterkonto an. Die App liest und schreibt dann über **Microsoft Graph** direkt in den freigegebenen Ordner. Ein eigener Server ist nicht nötig.

Benötigt wird eine **App-Registrierung in Microsoft Entra ID**. Aufwand für einen Admin: ca. 15 Minuten.

## 1. App registrieren

Entra Admin Center → **Identität → Anwendungen → App-Registrierungen → Neue Registrierung**

| Feld | Wert |
|---|---|
| Name | `EVSE-Prüfprotokoll` |
| Unterstützte Kontotypen | **Nur Konten in diesem Organisationsverzeichnis** (Single Tenant) |
| Umleitungs-URI – Plattform | **Single-Page-Anwendung (SPA)** |
| Umleitungs-URI – Adresse | `https://smarthomebutbetter.github.io/evse-pruefprotokoll/` |

Zieht die App später auf eine eigene Adresse um (z. B. `https://pruefung.elektro-irrgang.de/`), wird diese Adresse **zusätzlich** als SPA-Umleitungs-URI eingetragen.

Kein Client-Geheimnis und kein Zertifikat nötig: Die Anmeldung läuft als SPA mit PKCE.

## 2. API-Berechtigungen

**API-Berechtigungen → Berechtigung hinzufügen → Microsoft Graph → Delegierte Berechtigungen**

- `User.Read` – Name und E-Mail des angemeldeten Mitarbeiters
- `Files.ReadWrite.All` – Lesen/Schreiben im freigegebenen Ordner (im Namen des angemeldeten Nutzers, nur dort, wo der Nutzer ohnehin Rechte hat)
- `Mail.Send` – *optional:* fertige Prüfprotokolle direkt aus der App vom Konto des angemeldeten Mitarbeiters an info@elektro-irrgang.de senden (nur im Namen des angemeldeten Nutzers, kein Zugriff auf Postfächer)

Danach **„Administratorzustimmung für … erteilen“**.

*Alternative mit geringeren Rechten:* Liegt der Ordner auf einer **SharePoint-Teamwebsite** (nicht im OneDrive einer Person), kann statt `Files.ReadWrite.All` auch `Sites.Selected` verwendet werden; dann muss der Website zusätzlich gezielt Schreibzugriff für die App erteilt werden. Bitte kurz Bescheid geben, falls dieser Weg gewünscht ist.

## 3. App-Rolle „Admin“ (für die Geschäftsleitung)

In der App gilt: Jeder bearbeitet nur seine eigenen Prüfungen, sieht aber alle. Wer die Rolle **Admin** hat, darf alle bearbeiten und löschen.

1. App-Registrierung → **App-Rollen → App-Rolle erstellen**
   - Anzeigename: `Admin`
   - Zulässige Mitgliedstypen: **Benutzer/Gruppen**
   - Wert: `Admin` (genau so geschrieben)
   - Beschreibung: `Darf alle Prüfprotokolle bearbeiten`
2. **Unternehmensanwendungen → EVSE-Prüfprotokoll → Benutzer und Gruppen → Benutzer hinzufügen** → Geschäftsführer der Rolle **Admin** zuweisen.
3. Empfohlen: Unter **Eigenschaften** „Zuweisung erforderlich?“ = **Ja** und alle Mitarbeiter, die prüfen, zuweisen (ohne Rolle oder als Gruppe). Dann können sich nur diese Personen anmelden.

## 4. Ordner

- Ordner **„Prüfprotokolle“** auf einer SharePoint-Teamwebsite (empfohlen) oder im OneDrive der Geschäftsleitung.
- Alle prüfenden Mitarbeiter brauchen **Bearbeiten**-Rechte auf diesen Ordner.
- Benötigt wird der **Freigabe-Link** des Ordners (Ordner → Teilen → Link kopieren).

Die App legt darin an:

```
Prüfprotokolle/
  <Kunde>/<Standort>/[<Ladepark>/]<Datum> <Prüfart> <Auftragsnr>.pdf   ← lesbare PDFs
  _App-Daten/                                                        ← Daten der App, bitte nicht ändern
    kunden/  standorte/  ladeparks/  pruefungen/  fotos/
```

Empfehlung: Ordner auf einer SharePoint-Teamwebsite statt im persönlichen OneDrive, damit die Daten nicht an ein einzelnes Benutzerkonto gebunden sind.

## 5. Bitte zurückmelden

| Wert | Wo zu finden |
|---|---|
| **Verzeichnis-ID (Mandanten-ID)** | App-Registrierung → Übersicht |
| **Anwendungs-ID (Client-ID)** | App-Registrierung → Übersicht |
| **Freigabe-Link des Ordners** | Ordner → Teilen → Link kopieren |

Diese drei Werte werden in der App eingetragen (`CONFIG` am Anfang von `src/app.html`). Geheim sind sie nicht – es sind keine Passwörter.

## Optional: eigene Adresse

DNS-Eintrag bei der Domain elektro-irrgang.de:

```
pruefung   CNAME   smarthomebutbetter.github.io.
```

Vorteil: Die Adresse der App bleibt dauerhaft gleich, auch wenn das Hosting später wechselt (z. B. auf ein Firmenkonto). Ändert sich die Adresse, müssen die iPads die App neu zum Home-Bildschirm hinzufügen und lokale Daten per Sicherung übertragen.

## Gut zu wissen

- **Datenschutz:** Kundendaten liegen ausschließlich im Microsoft-365-Mandanten der Firma und auf den iPads. GitHub stellt nur die leere App bereit.
- **Offline:** Ohne Netz wird auf dem iPad gespeichert und später abgeglichen.
- **Rechte:** „Nur der Ersteller bearbeitet“ wird von der App durchgesetzt. Wer Schreibrechte auf den Ordner hat, könnte die Dateien technisch auch direkt in OneDrive/SharePoint ändern. Das ist bei einem gemeinsamen Ordner unvermeidbar; der Ordner `_App-Daten` sollte daher nicht von Hand bearbeitet werden.
- **Anmeldung:** Microsoft-Standardanmeldung (MSAL.js, Version 3.28.1, in die App eingebettet). Bedingter Zugriff und MFA des Mandanten gelten wie gewohnt.
