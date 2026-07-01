from faker import Faker

fake = Faker()

def extract_customers(count=10):
    customers = []

    for _ in range(count):
        customers.append(
            {
                "name": fake.name(),
                "email": fake.email(),
                "country": fake.country()
            }
        )

    return customers
