from database import connect_to_db

@app.get("/customers")
async def get_customers():
    try:
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM customers")  # Replace 'customers' with your table name
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return rows
        else:
            raise HTTPException(status_code=500, detail="Database connection failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
