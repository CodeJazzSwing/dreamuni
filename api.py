from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

class College(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    us_state: str
    birthdate: str
    major: str

class Advisor(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    major: str

app = FastAPI()

#Get all students
@app.get("/all")
def read_root():
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    query = """
    SELECT * FROM student
    """
    res = cur.execute(query) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data

#Get all advisors
@app.get("/alladvisors")
def read_root():
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    query = """
    SELECT * FROM advisor
    """
    res = cur.execute(query) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data

#Get with california state name
@app.get("/california")
def read_root():
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    query = """
    SELECT * FROM student WHERE us_state = 'CA';
    """
    res = cur.execute(query) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data

#Get with rolling state_id abbreviation
@app.get("/state/{state_id}")
def read_root(state_id):
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    res = cur.execute("SELECT * FROM student WHERE us_state = ?", [state_id]) 
    data = res.fetchall()
    cur.close()
    connection.close()
    return data

 

#Change majors.  
@app.put("/update_student")
def update_student(student: College):
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    res = cur.execute("UPDATE student SET major = ? WHERE id = ?", [student.major, student.id]) 
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return data

#Update advisor email address for mistakes
@app.put("/update_advisor")
def update_advisor(advisors: Advisor):
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    res = cur.execute("UPDATE advisor SET email = ? WHERE id = ?", [advisors.email, advisors.id]) 
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return data



@app.post("/create_student")
def create_student(student: College):
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    res = cur.execute("INSERT INTO student (first_name, last_name, email, us_state, birthdate, major) VALUES (?, ?, ?, ?, ?, ?)", 
        [student.first_name, student.last_name, student.email, student.us_state, student.birthdate, student.major])
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return(student)
 
@app.post("/create_advisor")
def create_advisor(advisors: Advisor):
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    res = cur.execute("INSERT INTO advisor (first_name, last_name, email, major) VALUES (?, ?, ?, ?)", 
        [advisors.first_name, advisors.last_name, advisors.email, advisors.major])
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return(advisors)
 
@app.delete("/delete_student/{id}")
def delete_student(id: int):
    connection = sqlite3.connect("unitable.db")
    cur = connection.cursor()
    res = cur.execute("DELETE FROM student WHERE id = ?", [id]) 
    data = res.fetchall()
    cur.close()
    connection.commit()
    connection.close()
    return data
