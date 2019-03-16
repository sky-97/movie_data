import movie_metadata
import sqlite3

def movieratings():
    conn = sqlite3.connect('movie.db')
    print ("Opened database successfully")
    cursor = conn.execute("SELECT  name,ratings/2 from movietable ORDER BY ratings/2 DESC")
    for row in cursor:
        print ("name = ", row[0])
        print ("ratings = ", row[1])
    return

def user_rating():
    rating = int(input("enter your ratings:"))
    if rating == 4:
        conn = sqlite3.connect('movie.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT name,ratings/2,genres from movietable WHERE ratings >='4';")
        for row in cursor:
            print ("name = ", row[0])
            print ("ratings = ", row[1])
            print ("genres = ", row[2])
    elif rating == 3:
        conn = sqlite3.connect('movie.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT name,ratings/2,genres from movietable WHERE ratings >='3';")
        for row in cursor:
            print ("name = ", row[0])
            print ("ratings = ", row[1])
            print ("genres = ", row[2])
    elif rating == 2:
        conn = sqlite3.connect('movie.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT name,ratings/2,genres from movietable WHERE ratings >='2';")
        for row in cursor:
            print ("name = ", row[0])
            print ("ratings = ", row[1])
            print ("genres = ", row[2])
    elif rating == 1:
        conn = sqlite3.connect('movie.db')
        print ("Opened database successfully")
        cursor = conn.execute("SELECT name,ratings/2,genres from movietable WHERE ratings >='1';")
        for row in cursor:
            print ("name = ", row[0])
            print ("ratings = ", row[1])
            print ("genres = ", row[2])
    return
def genre():
    conn = sqlite3.connect('movie.db')
    print ("Opened database successfully")
    cursor = conn.execute("SELECT name,genres from movietable")
    for row in cursor:
        print ("name = ", row[0])
        print ("genres = ", row[1])
    return

def rating_genre():
    conn = sqlite3.connect('movie.db')
    print ("Opened database successfully")
    cursor = conn.execute("SELECT name,ratings/2,genres from movietable ORDER BY genres DESC;")
    for row in cursor:
        print ("name = ", row[0])
        print ("ratings = ", row[1])
        print ("genres = ", row[2])
    return
def check_title():
    i = str(input("search movie title:"))
    conn = sqlite3.connect('movie.db')
    cursor = conn.execute("SELECT name from movietable WHERE name LIKE '%{}%'".format(i))
    for row in cursor:
        print ("name = ", row[0])
    return
def quit():
    return
