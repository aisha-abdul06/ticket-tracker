import sqlite3
from db import get_connection
connection = get_connection()

try:
  connection.execute(
   "ALTER TABLE tickets ADD COLUMN category_id INTEGER REFERENCES categories(id)"

 )
  print("Added category_id column.")
except sqlite3.OperationalError:
  print("Column already exists - skipping.")

  for name in ["Hardware", "Network", "Software", "Access"]:
   try:
    connection.execute(
     "INSERT INTO categories (name) VALUES (?)", (name,)
    )
   except sqlite3.IntegrityError:
    pass #UNIQUE stopped a duplicate; that's fine

   connection.commit()
   connection.close()
   print("Categories ready.")
   