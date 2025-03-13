import os
import sqlite3
import mysql.connector

header = """
             .__      __        ___.   .__                                        __                
  ___________|  |   _/  |______ \_ |__ |  |   ____     ___________   ____ _____ _/  |_  ___________ 
 /  ___/ ____/  |   \   __\__  \ | __ \|  | _/ __ \  _/ ___\_  __ \_/ __ \\__  \\   __\/  _ \_  __ \
 \___ < <_|  |  |__  |  |  / __ \| \_\ \  |_\  ___/  \  \___|  | \/\  ___/ / __ \|  | (  <_> )  | \/
/____  >__   |____/  |__| (____  /___  /____/\___  >  \___  >__|    \___  >____  /__|  \____/|__|   
     \/   |__|                 \/    \/          \/       \/            \/     \/                   
"""

# main menu 
print(header)
print("=> Pro Vytvoření nové tabulky napiš create ")
print("=> Pro exit napiš exit")

interakce = input("Zadejte interakci: ")

if interakce == "create":
    # SQLite připojení a vytvoření tabulky
    conn_sqlite = sqlite3.connect("database.db")
    cursor_sqlite = conn_sqlite.cursor()

    with open("table.sql", "r") as sql_file:
        cursor_sqlite.executescript(sql_file.read())

    conn_sqlite.commit()
    conn_sqlite.close()

    print("SQLite tabulka byla úspěšně vytvořena!")

    
    try:
        conn_mysql = mysql.connector.connect(
            host="localhost:2003",
            user="root",
            password="123",
            database="moje_databaze"
        )
        cursor_mysql = conn_mysql.cursor()

        cursor_mysql.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        );
        """)

        conn_mysql.commit()
        conn_mysql.close()

        print("MySQL tabulka byla úspěšně vytvořena!")

    except mysql.connector.Error as err:
        print(f"Chyba při připojení k MySQL: {err}")

else:
    print("Ukončuji program.")
    exit()
