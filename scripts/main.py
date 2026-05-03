from database_connection import get_connection
from database_transfer import *

choice = int(input('Welcome to your scraper. What do you want? \n'
'1. Testdatas into your Database \n'
'2. [Test] export Database Datas into CSV \n'
'3. [Test] export CSV Datas into the Database \n'))


if choice == 1: 
    create_testTable()
    close_Databases()
if choice == 2:
    test_export_to_csv()
if choice == 3: 
    test_import_from_csv()
