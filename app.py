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
    return jsonify({"name": "Alice", "age": 50})


if __name__ == "__main__":
    app.run(debug=True)