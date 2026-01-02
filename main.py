from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tinydb import TinyDB, Query

app = Flask(__name__)
CORS(app)

db = TinyDB("db.json")
user = Query()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=['POST'])
def add():
    query = request.get_json()
    title = query.get("title")
    text = query.get("text")
    date = query.get("date")
    
    if title and text and date:
        new_data = {
            "title": title,
            "text": text,
            "date": date,
            "completes": False
        }
        db.insert(new_data)
        return jsonify(db.all()), 201
    else:
        return jsonify({
            "error": "Ma'lumotlar to'liq emas", 
            "required": ["title", "text", "date"]
        }), 400

@app.route("/read", methods=['GET', 'POST'])
def read():
    return jsonify(db.all())


@app.route("/update", methods=['POST'])
def update():
    query = request.get_json()
    title = query.get("title")
    if title:
        db.update(query, user.title == title)
        return jsonify(db.all()), 200
    else:
        return 400

@app.route("/delete", methods=['GET'])
def delete():
    title = request.args.get("title")
    if title:
        db.remove(user.title == title)
        return jsonify(db.all())

if __name__ == "__main__":
    app.run(debug=True)
