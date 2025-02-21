import sqlite3

conn = sqlite3.connect('file_logs.db')
cursor = conn.cursor()

# Create table to store file integrity logs
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    hash TEXT,
    action TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
print("Database setup complete.")
