from faker import Faker

fake = Faker()

for i in range(10):
    print({
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country()
    })
