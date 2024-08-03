import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('testdb.sqlite')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Insert admin user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'password123'))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()

print("Database created and user inserted.")
