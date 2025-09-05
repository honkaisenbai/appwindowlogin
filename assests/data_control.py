import sqlite3
import json

config_file = open('./config.json')
config = json.load(config_file)

database = sqlite3.connect(config["database_files_path"])


db_control = database.cursor()

def on_startup():
    db_control.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT UNIQUE CHECK (length(phone) = 10 AND phone GLOB '[0-9]*')
        )
        """
    )
    db_control.execute("CREATE INDEX IF NOT EXISTS index_username ON users(username)")
    db_control.execute("CREATE INDEX IF NOT EXISTS index_email ON users(email)")
    db_control.execute("CREATE INDEX IF NOT EXISTS index_phone ON users(phone)")
on_startup()

def insert_data():
    db_control.execute("INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)",(username_data, password_data, email_data, phone_data))

try:
    insert_data()
    print("Data inserted successfully.")
except sqlite3.IntegrityError as e:
    print(f"Error inserting data: {e}")

database.commit()
database.close()