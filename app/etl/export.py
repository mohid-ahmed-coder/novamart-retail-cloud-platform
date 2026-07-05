import csv
import os

os.makedirs("data", exist_ok=True)

def export_customers(customers):
    with open("data/customers.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "email", "country"]
        )

        writer.writeheader()
        writer.writerows(customers)
