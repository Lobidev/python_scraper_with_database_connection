# Ein simpler Python Scraper mit MySQL-Datenbank Anbindung
***

## Beschreibung
Bei diesem Projekt wird von einer leglen Webseiten (siehe verlinkte Beispielseite ganz unten) die Daten transferiert aus der DOM-Struktur. Diese kann in den Funktionen folgendes: 

1. Die Daten werden von einer Webseite ausgelesen, eine Datenbank wird erstellt und diese werden in eine MySQL-Datenbank transferiert
2. Kann die Daten von einer Datenbank in eine CSV-Datei transferieren und umgekehrt
3. Es gibt Test Daten und Methoden, die das gleiche machen jedoch nicht von einer Webseite, sondern mit Testdaten getestet werden. 

## Wichtig !!
Dies ist ein Lernprojekt und wurde an einer Webseite durchgeführt, bei der Informationen frei zugänglich und ohne Authorisierung möglich war. Dieses Projekt ist nicht dafür vorgesehen für Illegale Zwecke missbraucht zu werden (umgehung von Authorisierung wie beispielsweise Logins). Wer dies tut macht sich strafbar! Bitte nur zum lernen oder nur aus öffentlichen Quellen die Informationen extrahieren (ansonsten den Webseiten betreiber fragen)




## Setup

1. Repo clonen
   git clone ...
   cd mein_projekt

2. Virtuelles Environment erstellen
   python3 -m venv venv
   source venv/bin/activate

3. Pakete installieren
   pip install -r requirements.txt

4. .env einrichten
   cp .env.example .env
   # .env öffnen und Werte anpassen

## Liste aller verwendeten Packages für dieses Projekt
1. MySQL-Connector-Python
2. Requests (Webseiten Abfragen) 
3. Beautifulsoup4  ("Scraping" Bibliotheken)
 
## Für alle die selbst Legal das lernen möchten kann man das auf der folgenden Webseite lernen
https://web-scraping.dev/ 
