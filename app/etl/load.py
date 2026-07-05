from psycopg2.extras import execute_batch
from app.database.connection import get_connection


def load_customers(customers):
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO customers(full_name,email,country)
        VALUES (%s,%s,%s)
        """

        data = [
            (
                c["name"],
                c["email"],
                c["country"]
            )
            for c in customers
        ]

        execute_batch(cursor, query, data)

        connection.commit()

        print(f"Loaded {len(customers)} customers.")

    except Exception as e:
        print("Database Error:", e)

        if connection:
            connection.rollback()

    finally:
        if connection:
            cursor.close()
            connection.close()
