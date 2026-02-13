# ETL Pipeline – Multi-format Data Processing

This project demonstrates the implementation of a complete
Extract, Transform, Load (ETL) pipeline using Python.

The pipeline processes structured data from multiple file formats
(CSV, JSON, and XML), applies transformations, and outputs a unified
dataset ready for loading into downstream systems.

---

## Project Objectives

- Extract data from heterogeneous sources
- Normalize and transform numerical fields
- Generate clean, load-ready output files
- Log execution steps for observability

---

## Technologies Used

- Python
- Pandas
- XML parsing
- File-based data ingestion
- Logging

---

## Project Structure

- `etl_code.py` - Functions to ETL pipeline implementation
- `execute_code.py` — Main ETL pipeline implementation
- `source` — Source and sample data files
- `transformed_data.csv` — Final transformed dataset
- `log_file.txt` — Execution logs
- `data_source/` — Practice exercise implementation

---

## ETL Workflow

1. **Extraction**
   - Reads CSV, JSON, and XML files
2. **Transformation**
   - Converts height (inches → meters)
   - Converts weight (pounds → kilograms)
   - Rounds values to two decimals
3. **Loading**
   - Writes transformed data to CSV
4. **Logging**
   - Records pipeline execution steps

---

## Practice Exercise

The `data_source/` directory contains an additional ETL exercise
implemented independently to reinforce the same concepts on a
different dataset.
