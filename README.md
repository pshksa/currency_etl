# Currency Rates ETL Project

## Описание
Проект демонстрирует полный цикл процесса ETL:
Извлечение данных о курсах валют из открытого API Центробанка России.
Обработка данных с использованием Pandas.
Загрузка данных в базу данных PostgreSQL.

Проект подходит для начальной практики в области Data Engineering.

## Технологии
- Python 3.10
- PostgreSQL
- Pandas
- Requests
- SQLAlchemy
- psycopg2

## Структура проекта

currency_etl/

├── scripts/

    ├── etl_functions.py

├── main.py

├── .env

├── requirements.txt

├── README.md

├── data/

├── check_table.py
