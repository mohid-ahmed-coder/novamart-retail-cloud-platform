# NovaMart v1 - Automated Customer ETL Pipeline

## Overview

NovaMart v1 is a modular ETL (Extract, Transform, Load) pipeline built to simulate a real-world customer data ingestion system.

This project was developed as a fictional client solution for an e-commerce company that required an automated way to process customer records before storing them in a database.

---

# Client

**Company:** NovaMart *(Fictional)*

**Industry:** E-commerce

---

# Business Problem

As NovaMart expanded, manually processing customer records became increasingly inefficient. The company required a solution capable of:

* Automating customer data processing
* Standardizing customer information
* Maintaining a backup of processed data
* Loading cleaned records into PostgreSQL
* Logging pipeline execution
* Supporting future cloud migration

---

# Solution

A modular ETL pipeline was designed using Python, Docker, and PostgreSQL.

The pipeline performs the following steps:

1. Generate customer data using Faker
2. Extract customer records
3. Transform and standardize the data
4. Export transformed records to CSV
5. Load processed records into PostgreSQL
6. Log pipeline execution

---

# Architecture

```text
                 Faker
                   │
                   ▼
         Extract Customer Data
                   │
                   ▼
      Transform Customer Data
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 customers.csv          PostgreSQL
        │                     │
        └──────────┬──────────┘
                   ▼
             Pipeline Logs
```

---

# Technology Stack

* Python
* PostgreSQL
* Docker
* Faker
* Git
* Linux (WSL)

---

# Project Structure

```text
novamart/

app/
└── etl/
    ├── extract.py
    ├── transform.py
    ├── export.py
    ├── load.py
    └── pipeline.py

data/
logs/

config.py
docker-compose.yml
requirements.txt
README.md
```

---

# Features

* Modular ETL architecture
* Dockerized PostgreSQL database
* CSV export
* Configurable pipeline
* Execution logging
* Clean separation of responsibilities
* Easy to extend with new data sources

---

# Pipeline Workflow

```
Extract
    │
    ▼
Transform
    │
    ▼
Export CSV
    │
    ▼
Load into PostgreSQL
    │
    ▼
Logging
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
cd novamart
```

Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start PostgreSQL

```bash
docker compose up -d
```

Run the pipeline

```bash
python -m app.etl.pipeline
```

---

# Example Output

The pipeline will:

* Generate customer records
* Transform the data
* Create `data/customers.csv`
* Insert records into PostgreSQL
* Update `logs/pipeline.log`

---

# Skills Demonstrated

* ETL Pipeline Development
* Python
* PostgreSQL
* Docker
* Linux
* Git
* Configuration Management
* Logging
* Data Engineering Fundamentals

---

# Future Improvements

The architecture has been intentionally designed to support future enhancements, including:

* AWS S3
* AWS Glue
* Amazon Athena
* Terraform
* Apache Airflow
* REST API integration
* Web scraping
* Kaggle datasets
* Cloud deployment

---

# Repository Status

**Version:** v1.0

This release represents the first stable version of the NovaMart ETL pipeline.

---

# Disclaimer

NovaMart is a fictional client created for portfolio purposes. The project demonstrates industry-standard ETL design principles using modern data engineering tools and practices.
