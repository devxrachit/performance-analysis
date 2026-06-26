from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect('novoguard.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/clinics/{clinic_id}")
def get_clinic(clinic_id: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clinics WHERE clinic_id = ?", (clinic_id,))
        clinic = cursor.fetchone()
        conn.close()
        
        if clinic is None:
            raise HTTPException(status_code=404, detail="Clinic not found")
        return dict(clinic)
        
    except sqlite3.OperationalError:
        raise HTTPException(status_code=404, detail="Database not initialized yet")