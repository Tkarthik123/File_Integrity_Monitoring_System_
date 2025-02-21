import sqlite3

conn = sqlite3.connect('file_logs.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM logs")
logs = cursor.fetchall()

print("=== File Change Logs ===")
for log in logs:
    print(log)

conn.close()
