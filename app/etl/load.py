from app.database.connection import get_connection

def load_customers(customers):
    connection = get_connection()
    cursor = connection.cursor()

    for customer in customers:
        cursor.execute(
            """
            INSERT INTO customers(full_name, email, country)
            VALUES (%s, %s, %s)
            """,
            (
                customer["name"],
                customer["email"],
                customer["country"]
            )
        )

    connection.commit()

    cursor.close()
    connection.close()
