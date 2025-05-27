MedAI – Anwendung zur medizinischen Bildverarbeitung
Dieses Projekt ist eine mehrsprachige Plattform zur Analyse medizinischer Bilder, die das Hochladen und Auswerten von MRT- (DICOM) und Röntgenbildern ermöglicht und Ärzt\*innen zur Unterstützung Empfehlungen geben kann.

🔍 Funktionen
Unterstützung für MRT- und Röntgenbilder (DICOM, JPEG/PNG)

KI-gestützte Segmentierung und Klassifikation

Mehrsprachige Oberfläche (TR / EN / DE)

Moderne Weboberfläche

Nutzung zur ärztlichen Entscheidungsunterstützung

Projektinhaber: Dr. M O

Unterstützt durch Muson Mühendislik

🧠 Modell
U-Net-Segmentierungsmodell auf Basis von PyTorch

Automatische Erkennung von krebsverdächtigen Geweben

🖥️ Installation

1. Backend
   bash
   Kopyala
   Düzenle
   cd backend
   pip install -r requirements.txt
   python app.py
2. Frontend (statische Dateien)
   Einfach frontend/index.html im Browser öffnen.

3. Docker (optional)
   bash
   Kopyala
   Düzenle
   docker build -t medai-app .
   docker run -p 8501:8501 medai-app
   🚀 Bereitstellung
   AWS EC2:
   EC2-Instanz erstellen

Dateien hochladen und Anwendung starten

Zugriff über http://<ip-adresse>:8501

AWS S3:
Ordner frontend/ auf S3 hochladen

Statisches Hosting aktivieren

📄 Lizenz
Dieses Projekt ist nicht für kommerzielle Zwecke bestimmt. Es dient ausschließlich der ärztlichen Entscheidungsunterstützung.

🧠 MedAI – Medizinische Bildanalyse-Anwendung
Diese Anwendung ermöglicht es, Röntgen- und MRT-(DICOM)-Bilder hochzuladen und eine KI-basierte Auswertung zu erhalten. Sie dient ausschließlich der ärztlichen Unterstützung.

📌 Ziel
Röntgen- oder DICOM-Bilder hochladen

Analyse mit KI-Modell durchführen

Ergebnisse visualisieren

Mehrsprachige Oberfläche (TR / EN / DE)

🩺 Zielnutzer
Fachärzt\*innen für Radiologie

Fachärzt\*innen für Pneumologie

Fachärzt\*innen für Orthopädie

📦 Projektstruktur

medai-app/
│
├── backend/ # Flask-basiertes Backend mit KI-Modell
│ ├── app.py # Hauptanwendung
│ ├── model/ # Modell- und Segmentierungsskripte
│ └── requirements.txt # Abhängigkeiten für das Backend
│
├── frontend/ # Statische Weboberfläche
│ └── index.html # Einstiegspunkt der Benutzeroberfläche
│
├── Dockerfile # Optionales Docker-Setup
├── README.md # Projektdokumentation
└── LICENSE # Lizenzinformationen
