import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Liest die .env Datei automatisch

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        unix_socket=os.getenv("DB_SOCKET"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )