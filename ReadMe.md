# Projekt: 2FA-Login und QR-Code-Generator

## Zweck des Projekts

Dieses Projekt implementiert ein einfaches Authentifizierungs- und Autorisierungssystem mit **Two-Factor Authentication (2FA)** sowie die Möglichkeit, QR-Codes basierend auf benutzerspezifischen Eingaben zu erstellen. Es beinhaltet:
1. **Login mit 2FA**: Der Benutzer meldet sich mit einem Benutzernamen und Passwort an und muss zusätzlich einen temporären 6-stelligen Code (generiert von einer Authenticator-App wie OpenOTP Token) eingeben.
2. **QR-Code-Generator**: Eine zusätzliche Funktion, die QR-Codes aus beliebigen Benutzereingaben generiert.

---

## Funktionsweise **(How to Use)**

1. **2FA Login**
   - Öffne die Login-Seite unter `/v1/login`.
   - Gib einen gültigen Benutzernamen und das zugehörige Passwort ein.
   - Nach erfolgreicher Anmeldung wird eine Seite mit einem QR-Code angezeigt. Scanne diesen QR-Code mit der **OpenOTP Token App** (oder einer anderen TOTP-basierenden App).
   - Der Benutzer gibt den in der App generierten TOTP-Code ein, um den Zugang zu bestätigen.

2. **QR-Code-Generator**
   - Navigiere zur QR-Code-Generator-Seite unter `/v1/totp/generate`.
   - Gib beliebigen Text in das Eingabefeld ein und drücke auf **„QR Code generieren“**.
   - Der generierte QR-Code wird im Browser angezeigt.

---

## Einrichtung der Entwicklungsumgebung **(Set up the Env)**

1. **Installiere Python**
   - Installiere [Python](https://www.python.org/downloads/) in Version 3.7 oder höher und füge es zu deinem System-Path hinzu.

2. **Virtuelle Umgebung einrichten**
   - Erstelle eine virtuelle Umgebung:
```shell script
python -m venv venv
```
   - Aktiviere die virtuelle Umgebung:
     - Windows:
```shell script
venv\Scripts\activate
```
     - macOS/Linux:
```shell script
source venv/bin/activate
```

---

## Abhängigkeiten installieren **(Install Dependencies)**

Alle benötigten Abhängigkeiten befinden sich in der `requirements.txt`. Installiere sie mit:

```shell script
pip install -r requirements.txt
```

Falls keine `requirements.txt` vorhanden ist, stelle sicher, folgende Pakete manuell zu installieren:

```shell script
pip install flask flask-bcrypt pyotp qrcode
```

---

## Anwendung starten **(Run the Application)**

1. Starte die Anwendung im Entwicklungsmodus:
```shell script
python user_app.py
```
2. Öffne den Browser und navigiere zu `http://127.0.0.1:5000`.

---

## Routen und Nutzung **(Routes and Usage)**

- **`/`**: Weiterleitung zur Login-Seite.
- **`/v1/login`** (`GET` und `POST`):
  - **GET**: Stellt das Login-Formular bereit.
  - **POST**: Prüft die Eingaben von Benutzername und Passwort. Bei Erfolg: Weiterleitung zur 2FA-Seite.
- **`/v1/verify`** (`POST`): Überprüft den eingegebenen TOTP-Code (6-stelliger Code aus der Authenticator-App). Bei Erfolg: Zugriff auf die geschützte Ressource.
- **`/v1/logout`** (`GET`): Loggt den Benutzer aus und löscht die Sitzungsdaten.
- **`/v1/totp/generate`** (`GET` und `POST`):
  - **GET**: Seite mit einer Eingabeoption für den QR-Code-Generator.
  - **POST**: Generiert einen QR-Code basierend auf dem eingegebenen Text.

---

## Abhängigkeiten **(What to Install?)**

Um dieses Projekt erfolgreich auszuführen, sind folgende Elemente erforderlich:

1. **Python Pakete**
   - Flask (für Webapplikation)
   - Flask-Bcrypt (für Passwort-Hashing)
   - PyOTP (für die TOTP-Verifizierung)
   - qrcode (für die QR-Code Generierung)

2. **Externe App**
   - **OpenOTP Token App**: Zum Scannen des QR-Codes und Generieren des 2FA-Codes:
     [OpenOTP Token App (Google Play)](https://play.google.com/store/apps/details?id=com.rcdevs.auth&hl=de&pli=1).

---

## So funktioniert die 2FA-Einrichtung

1. Der Benutzer meldet sich erfolgreich mit Benutzername und Passwort an.
2. Daraufhin wird ein geheimnisvoller Schlüssel (`2fa_secret`) generiert (z. B. `N4E6BAYA4GAQ5S3WSLAN73LCXNOTPRXQ`).
3. Ein QR-Code wird erstellt (basierend auf dem TOTP-Standard), den der Benutzer mit der **OpenOTP Token App** einscannen kann.
4. Nach dem Scannen generiert die App einen Code, den der Benutzer eingibt, um Zugriff zu erhalten.

Viel Erfolg mit dem Projekt!