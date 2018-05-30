from flask import Flask, render_template

from todo.db import TodoDB

app = Flask(__name__)


@app.route('/')
def hello():
    db = TodoDB()
    todo = db.read_all()
    return render_template("index.html", data=todo)

@app.route('/todo/<int:list_id>',methods=["DELETE"])
def delete(list_id):
    db = TodoDB()
    todo = db.delete_list(list_id)
    return "okey"


if __name__ == "__main__":
    app.run(debug=True)