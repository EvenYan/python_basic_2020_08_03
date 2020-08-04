from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Flask!"

@app.route("/home")
def home():
    return render_template("index1.html")


@app.route("/get_data")
def get_data():
    return jsonify({"goods_list": ["衬衫1","羊毛衫1","雪纺衫","裤子","高跟鞋","袜子"], \
        "sale_list": [5, 20, 36, 10, 10, 20]})


if __name__ == "__main__":
    app.run(debug=True)