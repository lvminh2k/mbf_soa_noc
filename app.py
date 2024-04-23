from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "this example of REST API Web Service"

@app.route("/get_submit_list")
def get_submit_list():
    submit_list = [
        {"id":1, "name": "Anna", "grade": "A"},
        {"id":2, "name": "Betty", "grade": "B"},
        {"id":3, "name": "Carlos", "grade": "C"},
        {"id":4, "name": "David", "grade": "D"},
        {"id":5, "name": "Flo", "grade": "F"}
    ]
    return jsonify(submit_list)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)