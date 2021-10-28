from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def register_form():
    return render_template("register.html")


@app.route('/join', methods=['POST'])
def adduser():
    name = request.form["name"]
    id = request.form["id"]
    password = request.form["password"]
    telephone = request.form["telephone"]

    with sql.connect('rabbit.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO rabbitUser(id, password, nickname, telephone) VALUES (?, ?, ?, ?)',
                    (id, password, name, telephone))
        con.commit()

    return "hi"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
