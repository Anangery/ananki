from crypt import methods
from email.policy import default
from multiprocessing.context import ForkContext
from tokenize import StringPrefix
import flask
import forms
import sqlite3 as sql

app = flask.Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'dSgUkXp2Xn2r5u8x'

def get_db_connection():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row
    return conn

@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    cards = conn.execute('SELECT * FROM cards').fetchall()
    name = conn.execute('SELECT * FROM name').fetchall()
    conn.close()
    form = forms.CardForm()
    forme = forms.NameForm()
    front = form.front.data
    back = form.back.data
    return flask.render_template("index.html", form=form, forme=forme, back=back, front=front, name=name, cards=cards)

@app.route('/name', methods=["POST", "GET"])
def name():
    conn = get_db_connection()
    cards = conn.execute('SELECT * FROM cards').fetchall()
    name = conn.execute('SELECT * FROM name').fetchall()
    conn.close()
    form = forms.CardForm()
    forme = forms.NameForm()
    front = form.front.data
    back = form.back.data

    if flask.request.method == "POST":
        name = forme.name.data
        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO name (name) VALUES (?)',
            (f'{name}', )
            )
            conn.commit()
            conn.close()
            return flask.render_template("index.html", form=form, forme=forme, back=back, front=front, name=name, cards=cards)
        except:
            return "Didn't work :(((("
    else:
        return flask.render_template("index.html", form=form, forme=forme, back=back, front=front, name=name, cards=cards)

@app.route("/send", methods=["POST", "GET"])
def add():
    form = forms.CardForm()
    forme = forms.NameForm()
    back = form.back.data
    front = form.front.data
    if flask.request.method == "POST":
        print('doing this')
        front = form.front.data
        back = form.back.data
        form.front.data = ''
        form.back.data = ''
        print(front, back)

        conn = get_db_connection()
        conn.execute('INSERT INTO cards (front, back) VALUES (?,?)',
        (front, back)
        )
        cards = conn.execute('SELECT * FROM cards').fetchall()
        name = conn.execute('SELECT * FROM name').fetchall()
        conn.commit()
        conn.close()

        return flask.render_template("index.html", form=form, forme=forme, back=back, front=front, name=name, cards=cards)
    else:
        conn = get_db_connection()
        cards = conn.execute('SELECT * FROM cards').fetchall()
        name = conn.execute('SELECT * FROM name').fetchall()
        conn.close()
        return flask.render_template("index.html", form=form, forme=forme, back=back, front=front, name=name, cards=cards)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute(f'DELETE FROM cards WHERE id={id}')
    conn.execute('DELETE FROM sqlite_sequence WHERE name=\'cards\'')
    conn.commit()
    conn.close()
    flask.flash('Deleted the entry')
    return flask.redirect('/')

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    return "Edit function not made"

@app.route("/finish", methods=['GET', 'POST'])
def finish():
    conn = get_db_connection()
    name = conn.execute('SELECT * FROM name').fetchall()
    conn.close()

    return flask.render_template("finish.html", name=name)

@app.route("/finishyes", methods=["POST"])
def finishyes():
    return "ok good"

@app.route("/finishno", methods=["POST"])
def finishno():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug=True)