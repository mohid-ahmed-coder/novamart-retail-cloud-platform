def transform_customers(customers):
    transformed = []

    for customer in customers:
        print(
            len(customer["country"]),
            customer["country"]
        )

        transformed.append(
            {
                "name": customer["name"].title(),
                "email": customer["email"].lower(),
                "country": customer["country"].upper(),
            }
        )

    return transformed
