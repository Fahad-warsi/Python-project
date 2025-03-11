import sqlite3

try:
    with sqlite3.connect("auth.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
            )""")
        print("Created table successfully")
except:
    conn.rollback()
    print("Transaction Failed...")
finally:
    conn.close()

#TESTING.....................
# with sqlite3.connect("auth.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users")
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
