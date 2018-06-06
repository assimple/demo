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
    data = request.get_json()
    db = TodoDB()
    todo = db.create(data['text'])
    db.close()
    return "okey"


@app.route('/todo/<int:list_id>', methods=["GET"])
def select(list_id):
    db = TodoDB()
    todo = db.select_list(list_id)
    print(todo)
    db.close()
    return jsonify({"existed": True}) if todo else jsonify({"existed": False})


@app.route('/todo/<int:list_id>', methods=["PUT"])
# 翻转状态 现在只有doing done
def flip_status(list_id):
    db = TodoDB()
    todo = db.read(list_id)
    if todo:
        status = todo[2]
        status = "done" if status == "doing" else "doing"
        db.update_status(list_id, status)
    db.close()
    return "okey"


@app.route('/123')
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
