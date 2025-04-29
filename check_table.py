# Проверка содержимого таблицы

import psycopg2

conn = psycopg2.connect(
    dbname="currency_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM currency_rates;")
count = cursor.fetchone()[0]

print(f"[INFO] В таблице currency_rates {count} записей.")

cursor.execute("SELECT * FROM currency_rates LIMIT 5;")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
