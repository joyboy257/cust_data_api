from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from datetime import datetime

# Load data from the provided Excel file
file_path = "small_haach_db.xlsx"

# Read the Excel file into a Pandas DataFrame
try:
    data = pd.read_excel(file_path)

    # Ensure proper column names (removing potential whitespace)
    data.columns = data.columns.str.strip()
except Exception as e:
    raise RuntimeError(f"Error reading Excel file: {str(e)}")

app = FastAPI(title="Customer Data API", description="API for EDA on customer data", version="1.0.0")

# Utility functions for EDA
def get_total_customers():
    return len(data)

def get_customers_above_age(age: int):
    if 'Date of Birth' in data.columns:
        current_year = datetime.now().year
        data['Age'] = data['Date of Birth'].apply(
            lambda dob: current_year - pd.to_datetime(dob, errors='coerce').year if pd.notnull(dob) else None
        )
        return len(data[data['Age'] > age])
    else:
        raise ValueError("The 'Date of Birth' column is not available in the dataset.")

def get_gender_distribution():
    if 'Gender' in data.columns:
        return data['Gender'].value_counts().to_dict()
    else:
        raise ValueError("The 'Gender' column is not available in the dataset.")

def get_branch_distribution():
    if 'Branch' in data.columns:
        return data['Branch'].value_counts().to_dict()
    else:
        raise ValueError("The 'Branch' column is not available in the dataset.")

def get_race_nationality_distribution():
    if 'Race/ Nationality' in data.columns:
        return data['Race/ Nationality'].value_counts().to_dict()
    else:
        raise ValueError("The 'Race/ Nationality' column is not available in the dataset.")

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Welcome to the Customer Data API!"}

@app.get("/total-customers")
async def total_customers():
    try:
        return {"total_customers": get_total_customers()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/customers-above-age/{age}")
async def customers_above_age(age: int):
    try:
        return {"customers_above_age": get_customers_above_age(age)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gender-distribution")
async def gender_distribution():
    try:
        return {"gender_distribution": get_gender_distribution()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/branch-distribution")
async def branch_distribution():
    try:
        return {"branch_distribution": get_branch_distribution()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/race-nationality-distribution")
async def race_nationality_distribution():
    try:
        return {"race_nationality_distribution": get_race_nationality_distribution()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
