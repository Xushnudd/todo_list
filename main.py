from flask import Flask, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB("db.json")
query = Query()

@app.route("/")
def home():
    return jsonify(db.all())

if __name__ == "__main__":
    app.run(debug=True)