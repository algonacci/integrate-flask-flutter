from flask import Flask, request, jsonify
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="eric",
    passwd="1234",
    database="attendance_ai",
)

cursor = db.cursor()

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    file = request.files["image"]
    name = request.form["name"]
    id_user = request.form["user_id"]
    time = request.form["time"]
    attendance_type = request.form["attendance_type"]
    print(file)
    print(name)
    print(id_user)
    print(time)
    print(attendance_type)
    if request.method == "POST":
        cursor.execute("""
        INSERT INTO `attendances` 
        (`id_user`, `name`, `time`, `attendance_type`)
        VALUES
        ('{}', '{}', '{}', '{}')
        """.format(id_user, name, time, attendance_type))
        db.commit()
        
        return jsonify({
        "status_code": 200,
        "message": "Success fetching the API",
        "prediction": "joshua",
        "confidence": 100,
        "time": time,
        "attedance_type": attendance_type
    })

if __name__ == "__main__":
    app.run(
        # host="192.168.1.104"
    )