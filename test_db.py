import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")

print("[DEBUG] DB_URL:", db_url)

try:
    conn = psycopg2.connect(
        dbname="currency_db",
        user="postgres",
        password="1234567890",
        host="localhost",
        port="5432"
    )
    print("[SUCCESS] Подключение к базе данных прошло успешно!")
    conn.close()
except Exception as e:
    print("[ERROR]", e)
