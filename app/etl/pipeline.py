from app.etl.extract import extract_customers
from app.etl.transform import transform_customers
from app.etl.load import load_customers

customers = extract_customers(100)

customers = transform_customers(customers)

load_customers(customers)

print("✅ ETL Pipeline Completed!")
