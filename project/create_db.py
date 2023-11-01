import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS candidate(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,year text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS forum(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS function(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(invoice INTEGER PRIMARY KEY AUTOINCREMENT,candidate text,name text,forum text,event_name text,price text,qty text,status text)")
    con.commit()
   
   
    

create_db()    