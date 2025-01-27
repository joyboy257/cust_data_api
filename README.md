This project provides a RESTful API for performing exploratory data analysis (EDA) on customer data extracted from an Excel file. The API is built using FastAPI and exposes insights in JSON format. It can compute total customers, gender distribution, branch distribution, and more.

Features

Total Customers: Retrieve the total number of customers.

Customers Above a Certain Age: Analyze the number of customers above a specified age.

Gender Distribution: Get the count of customers by gender.

Branch Distribution: Get customer counts per branch.

Race/Nationality Distribution: Analyze diversity among customers.

Project Structure

CUSTOMER-DATA-API/
├── main.py               # Main FastAPI application
├── database.py           # Database connection module
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (excluded from version control)
├── small_haach_db.xlsx   # Customer data (excluded from version control)
├── .gitignore            # Git ignore rules

Setup and Installation

Prerequisites

Python 3.11 or later

Pip (Python package installer)

Virtual Environment (recommended)

Steps

Clone the repository:

git clone https://github.com/your-username/customer-data-api.git
cd customer-data-api

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt

Add your .env file:
Create a .env file in the root directory with the following content:

DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database

Run the FastAPI application:

uvicorn main:app --reload

API Endpoints

Root

GET /: Welcome message and basic API information.

EDA Endpoints

GET /total-customers: Returns the total number of customers.

{
    "total_customers": 500
}

GET /customers-above-age/{age}: Returns the count of customers above a specified age.

{
    "customers_above_age": 120
}

GET /gender-distribution: Returns the gender distribution of customers.

{
    "gender_distribution": {
        "Male": 250,
        "Female": 250
    }
}

GET /branch-distribution: Returns the count of customers per branch.

{
    "branch_distribution": {
        "RC": 150,
        "C173": 200,
        "H40": 150
    }
}

GET /race-nationality-distribution: Returns the distribution of customers by race/nationality.

{
    "race_nationality_distribution": {
        "Chinese": 300,
        "Malay": 100,
        "Indian": 100
    }
}


