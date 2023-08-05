from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

    # Connect to an existing database
    conn = psycopg2.connect(host='localhost', 
    dbname='fastapi', 
    user='postgres',
    password='xxxxxxxxxx.',
    cursor_factory=RealDictCursor)

    # Open a cursor to perform database operations
    cursor = conn.cursor()

#creating an endpoint/path

@app.get("/users")
async def read_users():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return {"users": users}

cur.close()
conn.close()
