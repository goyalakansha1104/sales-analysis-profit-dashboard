"""
database.py
-----------
Connects Python to MySQL and fetches sales data.
"""

import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

# Load database settings from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "sales_analysis_db")


def get_db_connection():
    """Connect Python to the MySQL database."""

    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    return connection


def fetch_sales_data():
    """Fetch sales data from MySQL into a Pandas DataFrame."""

    query = """
        SELECT
            s.sale_id,
            s.order_date,
            c.customer_name,
            c.city,
            c.state,
            p.product_name,
            cat.category_name,
            p.unit_cost,
            p.unit_price,
            s.quantity,
            s.discount_percent,

            (p.unit_price * s.quantity)
            * (1 - s.discount_percent / 100)
            AS revenue,

            (p.unit_price - p.unit_cost)
            * s.quantity
            * (1 - s.discount_percent / 100)
            AS profit

        FROM sales s

        JOIN customers c
            ON s.customer_id = c.customer_id

        JOIN products p
            ON s.product_id = p.product_id

        JOIN categories cat
            ON p.category_id = cat.category_id

        ORDER BY s.order_date;
    """

    connection = get_db_connection()

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)

        rows = cursor.fetchall()
        columns = [item[0] for item in cursor.description]

        df = pd.DataFrame(rows, columns=columns)

        return df

    finally:
        cursor.close()
        connection.close()