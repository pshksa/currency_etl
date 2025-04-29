import requests
import pandas as pd
from sqlalchemy import create_engine
import os
import json
import psycopg2
import re

# ❗ Здесь НЕТ load_dotenv() ❗
# Переменные окружения читаем ВНУТРИ функций

def fetch_currency_data():
    """Скачать данные о курсах валют из API и сохранить в файл."""
    api_url = os.getenv("API_URL")
    data_dir = os.getenv("DATA_DIR", "data/")
    output_file = os.path.join(data_dir, "sample_response.json")

    os.makedirs(data_dir, exist_ok=True)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"[INFO] Данные успешно сохранены в {output_file}")
    else:
        raise Exception(f"[ERROR] Не удалось получить данные: код {response.status_code}")

def process_currency_data():
    """Обработать загруженные данные в DataFrame."""
    data_dir = os.getenv("DATA_DIR", "data/")
    input_file = os.path.join(data_dir, "sample_response.json")
    
    with open(input_file, encoding="utf-8") as f:
        data = json.load(f)
    
    currencies = data['Valute']
    df = pd.DataFrame(currencies).transpose()
    df = df[['CharCode', 'Name', 'Value', 'Previous']]
    df['Date'] = pd.to_datetime(data['Date'])
    
    print(f"[INFO] Данные успешно обработаны: {len(df)} записей")
    return df

def check_db_connection(db_url):
    """Проверить соединение с базой данных перед загрузкой."""
    print("[INFO] Проверка соединения с базой данных...")
    try:
        match = re.match(r'postgresql\+psycopg2://(.*?):(.*?)@(.*?):(.*?)/(.*?)$', db_url)
        if not match:
            raise Exception("Неверный формат строки подключения DB_URL")
        
        user, password, host, port, dbname = match.groups()

        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.close()
        print("[SUCCESS] Соединение с базой установлено успешно.")
    except Exception as e:
        print(f"[ERROR] Не удалось подключиться к базе данных: {e}")
        raise

def load_to_postgres(df):
    """Загрузить DataFrame в таблицу PostgreSQL."""
    db_url = os.getenv("DB_URL")
    table_name = os.getenv("TABLE_NAME", "currency_rates")

    check_db_connection(db_url)

    engine = create_engine(db_url)
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    print(f"[INFO] Данные успешно загружены в таблицу {table_name}")