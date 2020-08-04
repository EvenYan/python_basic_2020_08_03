from flask import Flask, render_template, jsonify, redirect, url_for, request


app = Flask(__name__)


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
    print(username, passwd)
    # {"thread_id": ["form", "args", "cookies"], }
    return render_template("user_center.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)