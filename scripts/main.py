from database_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS testdatas (
        Person_ID   INT PRIMARY KEY,
        firstname   VARCHAR(255),
        lastname    VARCHAR(255),
        description VARCHAR(1000)
    )
""")
print("✅ Tabelle 'testdatas' erstellt (oder existiert bereits).")

# Testdaten
testdaten = [
    (1,  "Anna",    "Müller",     "Anna arbeitet als Softwareentwicklerin in München und hat über 8 Jahre Erfahrung in der Webentwicklung."),
    (2,  "Ben",     "Schmidt",    "Ben ist Projektmanager bei einer Unternehmensberatung und leitet internationale Teams."),
    (3,  "Clara",   "Weber",      "Clara studiert Medizin im 6. Semester und engagiert sich ehrenamtlich im Roten Kreuz."),
    (4,  "David",   "Fischer",    "David ist selbstständiger Grafikdesigner und spezialisiert auf Corporate Identity und Branding."),
    (5,  "Eva",     "Bauer",      "Eva arbeitet als Lehrerin an einer Grundschule und hat eine Leidenschaft für kreative Pädagogik."),
    (6,  "Felix",   "Hoffmann",   "Felix ist Datenwissenschaftler bei einem Berliner Startup und beschäftigt sich mit Machine Learning."),
    (7,  "Greta",   "Koch",       "Greta ist Architektin und hat mehrere preisgekrönte Wohnbauprojekte in Hamburg realisiert."),
    (8,  "Hans",    "Richter",    "Hans ist pensionierter Ingenieur und gibt sein Wissen als Mentor an junge Berufseinsteiger weiter."),
    (9,  "Ida",     "Klein",      "Ida arbeitet als UX-Designerin und nutzt nutzerzentrierte Methoden zur Produktentwicklung."),
    (10, "Jonas",   "Wolf",       "Jonas ist Freelance-Fotograf und reist für Aufträge durch ganz Europa."),
    (11, "Klara",   "Schröder",   "Klara ist Rechtsanwältin mit Schwerpunkt Arbeitsrecht und vertritt Mandanten vor Gericht."),
    (12, "Leon",    "Neumann",    "Leon studiert Informatik im Master und forscht im Bereich Cybersicherheit."),
    (13, "Maria",   "Schwarz",    "Maria ist Ernährungsberaterin und hilft Klienten dabei, einen gesunden Lebensstil zu entwickeln."),
    (14, "Nico",    "Zimmermann", "Nico ist Mechatroniker und arbeitet in der Automobilindustrie an elektrischen Antriebssystemen."),
    (15, "Olivia",  "Braun",      "Olivia ist Marketingleiterin bei einem E-Commerce-Unternehmen und verantwortet das digitale Marketing."),
]

cursor.executemany(
    "INSERT INTO testdatas (Person_ID, firstname, lastname, description) VALUES (%s, %s, %s, %s)",
    testdaten
)
conn.commit()
print(f"✅ {cursor.rowcount} Testeinträge eingefügt.")

# Zur Überprüfung ausgeben
cursor.execute("SELECT * FROM testdatas")
rows = cursor.fetchall()

print("\n📋 Inhalt der Tabelle 'testdatas':")
print(f"{'ID':<5} {'Firstname':<12} {'Lastname':<15} {'Description'}")
print("-" * 90)
for row in rows:
    print(f"{row[0]:<5} {row[1]:<12} {row[2]:<15} {row[3][:60]}...")

cursor.close()
conn.close()
