from faker import Faker

from app.database.connection import get_connection

fake = Faker()

connection = get_connection()
cursor = connection.cursor()

for _ in range(10):
    cursor.execute(
        """
        INSERT INTO customers(full_name, email, country)
        VALUES (%s, %s, %s)
        """,
        (
            fake.name(),
            fake.email(),
            fake.country()
        )
    )

connection.commit()

cursor.close()
connection.close()

print("✅ 10 customers inserted!")
