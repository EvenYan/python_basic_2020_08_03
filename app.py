from flask import Flask, render_template, jsonify, redirect, url_for


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


if __name__ == "__main__":
    app.run(debug=True)