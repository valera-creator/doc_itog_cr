from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    data = {'1': '2'}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
