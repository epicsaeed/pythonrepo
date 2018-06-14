import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

conn = sqlite3.connect('Sdatabase.db')
print ("Opened database successfully")

#to be ran once
# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print ("Table created successfully")
conn.close()

#routes to the main page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_students():
    return render_template('students.html')

#adds record to database when recieving a post request
@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect("Sdatabase.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students VALUES (?,?,?,?)",(nm,addr,city,pin))
                con.commit()
                msg = "Record successfully added."
        except:
            con.rollback()
            msg = "Error in insertion process!"

        finally:
            con.close()
            return render_template("results.html",msg = msg)

#shows the elements of the list 
@app.route('/list')
def list():
    con = sqlite3.connect("Sdatabase.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    return render_template('list.html',rows = rows)


if __name__ == '__main__':
    app.run(debug = True)