import logging
import time

from config import CUSTOMER_COUNT
from app.etl.extract import extract_customers
from app.etl.transform import transform_customers
from app.etl.load import load_customers

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

start = time.time()

logging.info("Pipeline started.")

customers = extract_customers(CUSTOMER_COUNT)
logging.info(f"Extracted {len(customers)} customers.")

customers = transform_customers(customers)
logging.info("Transformation completed.")

load_customers(customers)
logging.info("Customers loaded into PostgreSQL.")

end = time.time()

logging.info(f"Pipeline completed in {end-start:.2f} seconds.")

print(f"✅ Pipeline completed in {end-start:.2f} seconds.")
