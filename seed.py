import json
import sqlite3


def call_db(query: str, values:list):
    print(query)
    connection = sqlite3.connect("unitable.db")
    cursor = connection.cursor()
    res = cursor.execute(query, values) #OBS! Executescript is for many. 
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data


with open("seed_student.json") as seed:   #r= open for default
    data = json.load(seed)
    for record in data:
        # print("Printing record...") #Do not need this line....Used as a test to see if printing.
        print(record)   
        call_db("INSERT INTO student (first_name, last_name, email, us_state, birthdate, major) VALUES (?, ?, ?, ?, ?, ?)", 
        [record.get("first_name"), record.get("last_name"), record.get("email"), record.get("us_state"), record.get("birthdate"), record.get("major")])


with open("seed_advisor.json") as seed:   
    data = json.load(seed)
    for record in data:
        print(record)   
        call_db("INSERT INTO advisor (first_name, last_name, email, major) VALUES (?, ?, ?, ?)", 
        [record.get("first_name"), record.get("last_name"), record.get("email"), record.get("major")])