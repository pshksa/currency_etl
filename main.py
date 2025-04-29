from dotenv import load_dotenv
import os

# Просто загружаем .env из текущей папки
load_dotenv()

from scripts.etl_functions import fetch_currency_data, process_currency_data, load_to_postgres


def main():
    print("[START] Запуск ETL-процесса для курсов валют...")
    
    fetch_currency_data()
    df = process_currency_data()
    load_to_postgres(df)

if __name__ == "__main__":
    print("[DEBUG] DB_URL:", os.getenv("DB_URL"))  # Проверка правильной строки
    print("[DEBUG REAL ENV] API_URL:", os.getenv("API_URL"))
    print("[DEBUG REAL ENV] DB_URL:", os.getenv("DB_URL"))
    main()
