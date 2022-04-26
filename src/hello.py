from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", title="flask test", name=name)


@app.route("/hello")
def hello2():
    name = request.args.get("name")
    return render_template("hello.html", title="flask test", name=name)


@app.route("/users")
def users():
    db = pymysql.connect(
        host="crudflask_mysql_db_1",
        user="user",
        password=("password"),
        db="testdb",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )
    cur = db.cursor()
    sql = "select * from users"
    cur.execute(sql)
    users = cur.fetchall()
    cur.close()
    db.close()
    return render_template("users.html", title="flask test", users=users)


@app.route("/health")
def good():
    name = "health"
    return name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
