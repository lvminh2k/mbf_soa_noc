from flask import Flask, jsonify, request
app = Flask(__name__)
submit_list = [
    {"id":1, "name": "Anna", "grade": "A"},
    {"id":2, "name": "Betty", "grade": "B"},
    {"id":3, "name": "Carlos", "grade": "C"},
    {"id":4, "name": "David", "grade": "D"},
    {"id":5, "name": "Flo", "grade": "F"}
]

@app.route("/")
def hello():
    return "this example of REST API Web Service"

@app.route("/get_submit_list")
def get_submit_list():
    return jsonify(submit_list)

@app.route("/get_student_by_id", methods=["POST"])
def get_student_by_id():
    id = request.json["id"]
    for (student in submit_list):
        if student["id"] == id:
            return student
    return {"message":"can not find student" + str(id)}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)