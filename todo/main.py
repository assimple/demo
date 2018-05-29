from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    todo=[
        "测试1",
        "测试2",
        "测试3",
        "测试4",
        "测试5"
    ]
    return render_template("index.html", data=todo)


if __name__=="__main__":
    app.run(debug=True)
