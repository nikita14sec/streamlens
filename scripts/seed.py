import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/streamlens.db")
cur = conn.cursor()

# ---------------- USERS ----------------
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")

cur.executemany(
    "INSERT INTO users VALUES (?, ?)",
    [
        (1, "alice"),
        (2, "bob"),
        (3, "charlie"),
        (4, "david"),
    ]
)

# ---------------- ORDERS (for JOIN) ----------------
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("CREATE TABLE orders (id INTEGER, user_id INTEGER)")

cur.executemany(
    "INSERT INTO orders VALUES (?, ?)",
    [
        (101, 1),
        (102, 2),
        (103, 2),
    ]
)

conn.commit()
conn.close()

print("✅ Database seeded")