from flask import Flask, render_template, jsonify, redirect, url_for, request
from tools import gen_secret
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qaz@WSX@127.0.0.1:3306/flask_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    passwd = db.Column(db.String(200))


@app.route("/old_url")
def old_url():
    url = url_for("new_url")
    return redirect(url)


@app.route("/new2_url")
def new_url():
    return "全新接口！"


@app.route("/", methods=["POST"])
def index():
    return "Hello Flask!"

@app.route("/home")
def home():
    return render_template("index1.html")


@app.route("/get_data")
def get_data():
    return jsonify({"goods_list": ["衬衫1","羊毛衫1","雪纺衫","裤子","高跟鞋","袜子"], \
        "sale_list": [5, 20, 36, 10, 10, 20]})


@app.route("/post/<int:post_id>")
def get_post(post_id):
    return "这是第%d篇文章"%post_id


@app.route("/s")
def search_by_kw():
    kw = request.args.get("wd")
    return "搜索的关键字为：%s"%kw


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/deal_register", methods=["POST"])
def deal_register():
    username = request.form.get("username")
    passwd = request.form.get("passwd")
    passwd = gen_secret(passwd)
    user = User(name=username, passwd=passwd)
    db.session.add(user)
    db.session.commit()
    print(username, passwd)
    # {"thread_id": ["form", "args", "cookies"], }
    return render_template("user_center.html", username=username)


@app.route("/insert_data")
def insert_data():
    user1 = User(name="Tom", passwd="abc")
    db.session.add(user1)
    db.session.commit()
    return "数据插入成功！"


@app.route("/search_data")
def search_data():
    id = request.args.get("id")
    user = User.query.get(id)
    print(user.name)
    return "查找成功！"

@app.route("/update_data")
def updata_data():
    name = request.args.get("name")
    user = User.query.get(1)
    user.name = name
    db.session.add(user)
    db.session.commit()
    return "数据修改成功！"


@app.route("/delete_data")
def delete_data():
    id = request.args.get("id")
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "数据删除成功！"


if __name__ == "__main__":
    app.run(debug=True)