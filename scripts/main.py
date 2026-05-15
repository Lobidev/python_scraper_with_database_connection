from database_connection import get_connection
from database_transfer import *

choice = int(input('==================================\n'
'Willkommen zum Scraper was möchtest du gerne tun? \n'
'=============1. Scraper Menü ================= \n'
'1. Daten scrapen und in eine Datenbank speichern \n'
'2. Daten von CSV in eine Datenbank speichern \n'
'3. Datenbank Daten in eine CSV-Datei speichern \n'
'=============2. Test (mit Testdaten) Menü ================= \n'
'4. Testdaten generieren und in eine Datenbank speichern \n'
'5. Daten von CSV in eine Datenbank speichern \n'
'6. Datenbank Daten in eine CSV-Datei speichern \n'
'================================== \n'
'Eingabe: '
))

match choice:
    case 1: 
         create_quoteTable()
         close_databases()
    case 2:
        import_csv_to_database()
    case 3:
        import_database_to_csv()
    case 4:
        create_testTable()
        close_databases()
    case 5:
        test_import_from_csv()
    case 6:
        test_export_to_csv()
    


   
