from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route("/")
def hello():
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
    return render_template("hello.html", title="flask test", users=users)


@app.route("/good")
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
