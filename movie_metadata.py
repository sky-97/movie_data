import csv
import sqlite3
#
conn = sqlite3.connect('movie.db')
# c = conn.cursor()
# c.execute("""create table movietable (name TEXT,ratings REAL,genres TEXT)""")
def database():
    with open('movie_metadata.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            c.execute("INSERT into movietable values (?,?,?)",(str(line[11]),float(line[25]),str(line[9])))
    return 

#database()
conn.commit()
conn.close()
