# 🚀 Databricks Medallion Architecture Pipeline (DLT_Root)

This project demonstrates an **end-to-end data engineering pipeline** built on **Databricks** using the **Medallion Architecture** (Bronze → Silver → Gold).  
It is part of my **portfolio work**, showcasing how raw data can be ingested, transformed, and curated into business-ready datasets that solve **real-world data challenges**.

---

## 🏗️ Architecture Overview

The pipeline follows the **Medallion Architecture** pattern:

- **Bronze Layer** 🟤  
  Raw data ingestion with minimal transformations. Stores data in its original format for traceability.  

- **Silver Layer** ⚪  
  Cleansed and standardized data with schema enforcement, deduplication, Slowly Changing Dimensions (SCD Type 1 & 2), and data quality checks.  

- **Gold Layer** 🟡  
  Aggregated and curated data optimized for reporting, analytics, and downstream machine learning use cases.  

📌 Implemented using **Databricks Delta Live Tables (DLT)**, supporting both **batch and streaming** workloads.

---

## 📂 Repository Structure

DLT_Root/
│
├── bronze/ # Raw ingestion layer (landing data)
├── silver/ # Cleansed and transformed datasets
├── gold/ # Business-ready curated datasets
├── notebooks/ # Databricks notebooks (.py/.ipynb)
├── pipeline/ # Declarative pipeline YAML/JSON configs
├── sample_data/ # Example data for testing
└── docs/ # Documentation and architecture diagrams
