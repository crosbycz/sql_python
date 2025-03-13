import os
import sqlite3
import psycopg2  
import json

header = """
             .__      **        **_.   .__                                        __                
  ___________|  |   */  |*_____ \_ |__ |  |   ____     ___________   ____ _____ */  |*  ___________
 /  ___/ ____/  |   \   **\**  \ | __ \|  | */ *_ \  */ *__\_  __ \_/ ** \\**  \\   **\/  ***** \*****  ** \
 \___ < <_|  |  |__  |  |  / __ \| \_\ \  |_\  ___/  \  \___|  | \/\  ___/ / __ \|  | (  <_> )  | \/
/____  >__   |____/  |__| (____  /___  /____/\___  >  \___  >__|    \___  >____  /__|  \____/|__|  
     \/   |__|                 \/    \/          \/       \/            \/     \/                  
"""

# main menu
print(header)
print("=> Pro Vytvoření nové tabulky napiš create ")
print("")
print("=> Pro exit napiš exit")
interakce = input("Zadejte interakci: ")

if interakce == "create":
   
    conn_sqlite = sqlite3.connect("database.db")
    cursor_sqlite = conn_sqlite.cursor()
    with open("table.sql", "r") as sql_file:
        cursor_sqlite.executescript(sql_file.read())
    conn_sqlite.commit()
    conn_sqlite.close()
    print("SQLite tabulka byla úspěšně vytvořena!")
   
    try:
        
        conn_postgres = psycopg2.connect(
            host="localhost",
            user="postgres",  
            password="123",   
            port=5432         
        )
        conn_postgres.autocommit = True  
        cursor_postgres = conn_postgres.cursor()
        
        
        cursor_postgres.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'moje_databaze'")
        exists = cursor_postgres.fetchone()
        
        if not exists:
            cursor_postgres.execute("CREATE DATABASE moje_databaze")
        
        
        conn_postgres.close()
        
        
        conn_postgres = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="123",
            port=5432,
            database="moje_databaze"
        )
        cursor_postgres = conn_postgres.cursor()
        
        
        cursor_postgres.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        );
        """)
        conn_postgres.commit()
        conn_postgres.close()
        print("PostgreSQL tabulka byla úspěšně vytvořena!")
    except Exception as err:
        print(f"Chyba při připojení k PostgreSQL: {err}")
else:
    print("Ukončuji program.")
    exit()