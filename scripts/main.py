from database_connection import get_connection
from database_transfer import *

choice = int(input('Welcome to your scraper. What do you want? \n'
'1. Testdatas into your Database '))


if choice == 1: 
    create_testTable()
    close_Databases()
