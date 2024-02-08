import Adafruit_DHT
import sqlite3
from datetime import datetime
from time import sleep

# SQL - Opret table hvis den ikke findes
query = """SELECT * FROM dht11 LIMIT 20;"""
try: # Forbind til database og opret table
    conn = sqlite3.connect("dht11_data.db")
    # som standard returneres forspørgsler som tuples
    # men man kan ogs bruge row factory til at modtage dem i dictionary format
    # se: https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query)
    rows = result.fetchall()
    for row in rows:   
        print(f"""\ttimestamp: {row["datetime"]}\n
        temperature: {row["temperature"]}\n
        humidity: {row["humidity"]}\n""")

except sqlite3.Error as e: # Vis fejlmeddelse hvis den fejler
    print(f"Error : {e}")
    
finally: # Lukker database forbindelse
    conn.close()