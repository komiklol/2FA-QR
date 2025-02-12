# 2FA Login und QR Code Generator - Flask Anwendung

Dieses Projekt kombiniert einen **2FA (Two-Factor Authentication)-Login** mit einem **QR Code Generator**, entwickelt mithilfe des Flask Frameworks. Die Anwendung erlaubt es Nutzern, eine sichere Anmeldung mit 2FA durchzuführen und QR-Codes aus beliebigen Eingaben zu generieren.

---

## Wofür ist diese Anwendung? **(What is it for?)**

Diese Anwendung bietet zwei Hauptfunktionen:

### 1. **2FA Login-System**
- Implementiert ein Login-System mit Benutzernamen/Passwort sowie einer zusätzlichen Sicherheitsprüfung durch einen 2FA-Code (basiert auf **TOTP**).
- Der Benutzer scannt einen QR-Code (generiert von der Anwendung) mit einer Authenticator-App (z. B. OpenOTP Token), um TOTP-Codes zu generieren.

### 2. **QR Code Generator**
- Bietet die Möglichkeit, **dynamisch QR-Codes** zu erstellen, die entweder per API oder über ein Webformular generiert und direkt als Bild dargestellt werden.

---

## Nutzung der Anwendung **(How to Use It)**

### 1. Repository klonen **(Clone the Repository)**

Klonen Sie das Repository in Ihr Arbeitsverzeichnis:

```shell script
git clone https://github.com/komiklol/2FA-QR
cd 2FA-QR
```

---

### 2. Umgebung einrichten **(Set Up the Environment)**

Richten Sie eine virtuelle Umgebung ein, um Abhängigkeiten isoliert zu installieren:

```shell script
# Virtuelle Umgebung erstellen
python -m venv venv

# Aktivieren Sie die virtuelle Umgebung
# Für Windows
venv\Scripts\activate

# Für macOS und Linux
source venv/bin/activate
```

---

### 3. Abhängigkeiten installieren **(Install Dependencies)**

Installieren Sie die erforderlichen Python Pakete mit:

```shell script
pip install Flask flask-bcrypt pyotp qrcode[pil]
```

---

### 4. Anwendung starten **(Run the Application)**

Starten Sie die Flask-Anwendung:

```shell script
flask --app user_app.py run
```

Standardmäßig wird die Anwendung unter **http://127.0.0.1:5000** bereitgestellt.

---

## Routen und Nutzung **(Routes and Usage)**

| **Route**               | **Beschreibung**                                                                                   |
|-------------------------|----------------------------------------------------------------------------------------------------|
| **`/`**                 | Weiterleitung zur Login-Seite.                                                                     |
| **`/v1/login`**         | Login-Seite: Filtert Anmeldedaten (Nutzername/Passwort) und startet bei Erfolg den 2FA-Prozess.    |
| **`/v1/verify`**        | Prüft den eingegebenen **2FA-Code** und gibt den Zugang frei, wenn der Code korrekt ist.           |
| **`/v1/logout`**        | Loggt den Benutzer aus und löscht Sitzungscookies.                                                 |
| **`/v1/totp/generate`** | QR-Code Generator: Generiert QR-Codes aus Texteingaben (per Formular) und zeigt sie im Browser an. |

---

## Benutzung des 2FA-Workflows

1. Der Benutzer gibt erfolgreiche Anmeldedaten (Benutzername/Passwort) ein. (Name: testuser, Passwort: qwert123)
2. Ein QR-Code wird angezeigt, den der Benutzer mit einer Authenticator-App scannen kann (z. B. [OpenOTP Token](https://play.google.com/store/apps/details?id=com.rcdevs.auth)).
3. Der Benutzer gibt den in der App erhältlichen TOTP-Code ein, um die Anmeldung abzuschließen.

---

## Erforderliche Installation

Für dieses Projekt werden folgende Abhängigkeiten benötigt:

1. **Python-Bibliotheken**
   - **Flask**: Web Framework für die Anwendung.
   - **Flask-Bcrypt**: Hashing von Passwörtern für die Sicherheit.
   - **PyOTP**: Implementierung des TOTP-Standards für 2FA.
   - **qrcode**: Bibliothek zur Generierung von QR-Codes.

2. **Empfohlene Tools**
   - Authenticator-App: **[OpenOTP Token App](https://play.google.com/store/apps/details?id=com.rcdevs.auth)** zum Scannen der generierten QR-Codes und zur Erzeugung von TOTP-Codes.

---

## Hinweise

- **TOTP-Code Ablauf:** Die von der Authenticator-App generierten Codes sind für jeweils 30 Sekunden gültig.
- **Sicherheit:** Sitzungscookies werden verwendet, um Benutzersitzungen zu verwalten.

---

## Viel Spaß mit dem 2FA Login System und QR Code Generator! 🚀