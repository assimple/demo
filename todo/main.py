from flask import Flask, render_template, jsonify, request

from todo.db import TodoDB

app = Flask(__name__)


@app.route('/')
def index():
    db = TodoDB()
    todo = db.read_all()
    db.close()
    return render_template("index.html", data=todo)


@app.route('/todo/<int:list_id>', methods=["DELETE"])
def delete(list_id):
    db = TodoDB()
    todo = db.delete_list(list_id)
    result = db.read(list_id)
    db.close()
    return jsonify({"existed": True}) if result else jsonify({"existed": False})


@app.route('/todo', methods=["POST"])
def add():
    data=request.get_json()
    db = TodoDB()
    todo = db.create(data['text'])
    db.close()
    return "okey"


if __name__ == "__main__":
    app.run(debug=True)