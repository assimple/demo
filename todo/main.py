from flask import Flask, render_template

from todo.db import TodoDB

app = Flask(__name__)


@app.route('/')
def hello():
    db=TodoDB()
    todo=db.read_all()
    return render_template("index.html", data=todo)


if __name__=="__main__":
    app.run(debug=True)
