import sqlite3

connection = sqlite3.connect("unitable.db")


def call_db(student_query: str):
    print(student_query)
    connection = sqlite3.connect("unitable.db")
    cursor = connection.cursor()
    res = cursor.execute(student_query) #OBS! Executescript is for many. 
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data

student_query = """
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR (255),
    last_name VARCHAR (255),
    email VARCHAR (100),  
	us_state VARCHAR (50), 
	birthdate DATE,
	major VARCHAR (50)
);
"""

def call_db(advisor_query: str):
    print(advisor_query)
    connection = sqlite3.connect("unitable.db")
    cursor = connection.cursor()
    res = cursor.execute(advisor_query) #OBS! Executescript is for many. 
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data

advisor_query = """
CREATE TABLE IF NOT EXISTS advisor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR (255),
    last_name VARCHAR (255),
    email VARCHAR (100),  
	major VARCHAR (50)
);
"""


data = call_db(student_query)
data = call_db(advisor_query)

print(data)