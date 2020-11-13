"""
Read data from the candidates.txt file and enter it into a candidates table. This should be similar to the one created in Lecture 20.

Hints:

Copy the necessary set-up from the cells in Lecture 20.
Be careful not to copy blindly! You will get an error if you do.
To skip the header in candidates.txt you can use the next() method.
You will need to do a little processing on the input to split along the | characters.

Pair Programming Week 11

Team Members: Teresa Datta, Victoria DiTomasso, Junkai Ong
"""

import sqlite3
import numpy as np

# Reading in the file
text = np.loadtxt('candidates.txt',dtype='str',delimiter='|',skiprows=1)

db = sqlite3.connect('candidates')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over
cursor.execute("DROP TABLE IF EXISTS contributors") # Convenient in case you want to start over

cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_name TEXT, 
               party TEXT NOT NULL)''')

db.commit()

for t in text:  
    cursor.execute('''INSERT INTO candidates
               (id, first_name, last_name, middle_name, party)
               VALUES (?, ?, ?, ?, ?)''', 
                t )
    db.commit()

# cursor.execute("SELECT * FROM candidates")
# all_rows = cursor.fetchall()
# print(all_rows)
