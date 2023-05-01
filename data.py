import sqlite3
import hashlib


conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS data (
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "kaviul", hashlib.sha256(
    "kavpass".encode()).hexdigest()
username2, password2 = "nowshin", hashlib.sha256(
    "nowshin".encode()).hexdigest()
username3, password3 = "farhan", hashlib.sha256(
    "farhanpass".encode()).hexdigest()

cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username1, password1))
cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username2, password2))
cur.execute("INSERT INTO data (username, password) VALUES (?, ?)",
            (username3, password3))

conn.commit()
