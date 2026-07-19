import sqlite3

conn = sqlite3.connect("finance_system.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    expense_date TEXT,
    user_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS budget(
    budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
    monthly_budget REAL,
    month INTEGER,
    year INTEGER,
    user_id INTEGER
)
""")

conn.commit()

conn.close()