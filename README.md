# EVSE-Prüfprotokoll – Einrichtung für die iPads

Die App besteht aus zwei Dateien:

- `index.html` – die komplette App (inkl. PDF-Erstellung, läuft offline)
- `sw.js` – sorgt dafür, dass die App nach dem ersten Öffnen auch ohne Internet startet

`icon-180.png` ist nur das App-Symbol zum Ansehen, es steckt bereits in `index.html`.

## 1. Einmal ins Netz stellen (z. B. GitHub Pages, kostenlos)

1. Auf github.com ein neues Repository anlegen, z. B. `evse-pruefprotokoll` (öffentlich).
2. `index.html` und `sw.js` hochladen („Add file → Upload files“).
3. Settings → Pages → Source: „Deploy from a branch“, Branch `main`, Ordner `/ (root)` → Save.
4. Nach ca. 1 Minute ist die App erreichbar unter
   `https://<benutzername>.github.io/evse-pruefprotokoll/`

Alternativ geht jeder Webspace mit **https** (z. B. der der Firma).

Auf dem Server liegen **keine Kundendaten** – nur die leere App.

## 2. Auf jedem iPad

1. Adresse in **Safari** öffnen.
2. Teilen-Symbol → **„Zum Home-Bildschirm“** → Hinzufügen.
3. Ab jetzt über das Symbol „EVSE-Prüfung“ starten.

## 3. Im Alltag

- **+ Neues Protokoll** → Projekt, Ladesäulen, Messwerte eintragen. Speichert automatisch auf dem iPad.
- **PDF erstellen** → das PDF wird heruntergeladen. Über Teilen → „In Dateien sichern“ oder per Mail weitergeben.
- **Als Vorlage kopieren** → gleiche Säulen, leere Messwerte (für die nächste Wiederholungsprüfung).

## 4. Wichtig: Sichern

Die Protokolle liegen **nur auf dem jeweiligen iPad** im Browser-Speicher.
Safari kann diesen Speicher leeren (z. B. „Verlauf und Websitedaten löschen“ oder wenn die App lange nicht benutzt wurde).

- Regelmäßig in der Liste unten auf **„Alle sichern“** tippen → Datei in „Dateien“ oder per Mail ablegen.
- **„Sicherung laden“** liest so eine Datei wieder ein, auch auf einem anderen iPad. Bereits vorhandene Protokolle werden nicht doppelt angelegt; die neuere Fassung gewinnt.

Das fertige **PDF** ist das eigentliche Prüfprotokoll – das gehört immer zusätzlich in eure Ablage.

## 5. Update der App

Neue `index.html` hochladen und in `sw.js` die Zeile `const CACHE = "evse-v1";` auf `evse-v2` usw. erhöhen und ebenfalls hochladen. Die iPads holen sich die neue Version beim nächsten Öffnen mit Internet.

## Für Entwickler

- Quelltext der App: `src/app.html`
- `python3 tools/build.py` baut daraus `index.html` (bettet `vendor/jspdf.umd.min.js` und das Icon ein).
- Nach jeder Änderung in `sw.js` die Cache-Version erhöhen.
