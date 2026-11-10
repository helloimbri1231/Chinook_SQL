import os
import sqlite3

# --- 1. KEEP THIS SETUP ---
# Automatically finds the database in the same folder
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Chinook_Sqlite.sqlite")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# --- 2. CHANGE THIS QUERY ---
query = """
SELECT AlbumId, Name, Title FROM Artist LEFT JOIN Album ON Album.ArtistId = Artist.ArtistId WHERE AlbumId IS NULL;
"""

# --- 3. KEEP THIS EXECUTION ---
for row in cursor.execute(query):
    print(row) 

conn.close()