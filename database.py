import sqlite3

#to connect to database & creates database file
conn = sqlite3.connect("bank.db")

#cursor allowing me to run SQL commands
cursor = conn.cursor()

#accounts table
#CREATE TABLE makes a table called accounts with columns id/account number, name, and balance
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
 """)

conn.commit()
conn.close()

print("Database Ready!")

