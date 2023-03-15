from flask import Flask,render_template,request
import sqlite3 as sql
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disp')
def disp():
    return render_template('display.html')

@app.route('/dis',methods=['POST','GET'])
def dis():
    mag = []
    place = []
    mag1 = request.form.get('m1')
    mag2 = request.form.get('m2')
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("select count(mag),place from earthquake where ?< mag and mag<? group by mag",[mag1,mag2])
    data = cur.fetchall()
    for i in data:
        mag.append(i[0])
        place.append(i[1])
    print(place)
    return render_template('display.html',labels = place,values = mag,mag1 = mag1,mag2 = mag2)


# Question2
@app.route("/i2")
def index2():
    return render_template("question2.html")

@app.route("/question2", methods=['GET','POST'])
def question2():
    labels=[]
    values=[]
    r1=float(request.form.get('r1'))
    con= sql.connect("database.db")
    cur=con.cursor()
    cur.execute("select mag, count(mag),substr(time,12,8) as time from earthquake where mag>? and time not between '06:00:00' and '18:00:00' group by mag",[r1])
    data=cur.fetchall()
    for i in data:
        labels.append(i[0])
        values.append(i[1])
    return render_template("question2.html",labels=labels, values=values)


# Question3
@app.route("/i3")
def index3():
    return render_template("question3.html")

@app.route("/question3", methods=['GET','POST'])
def question3():
    labels=[]
    values=[]
    r1=request.form.get('r1')
    con= sql.connect("database.db")
    cur=con.cursor()
    cur.execute("select count(*), mag, place from earthquake where place LIKE '%"+str(r1)+"' group by mag")
    data=cur.fetchall()
    for i in data:
        labels.append(i[2])
        values.append(i[0])
    return render_template("question3.html",labels=labels, values=values)

if __name__ == "__main__":
    app.run( port = 5001,debug=True)