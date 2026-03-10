# Accessing Databases using Python

This project demonstrates how to interact with relational databases using Python.

## Objective

Create a database using SQLite, load data from a CSV file, and run SQL queries using Python.

## Technologies

- Python
- SQLite3
- Pandas

## Dataset

The dataset contains instructor records with the following fields:

| Column | Description |
|------|------|
| ID | Employee ID |
| FNAME | First Name |
| LNAME | Last Name |
| CITY | City of residence |
| CCODE | Country code |

## Workflow

1. Create a SQLite database (`STAFF.db`)
2. Load CSV data into a table (`INSTRUCTOR`)
3. Execute SQL queries using Pandas
4. Append new data into the table

## Example Queries

- Retrieve all rows
- Retrieve only instructor names
- Count number of records

## Practice Problems

Additional exercises were implemented in the `practice_problems` directory, including:

- Creating a `Departments` table
- Loading data from a CSV file
- Running SQL queries on the new table

## Learning Outcome

This project demonstrates how Python can be used as an interface for:

- Database creation
- ETL workflows
- SQL querying
- Data manipulation
