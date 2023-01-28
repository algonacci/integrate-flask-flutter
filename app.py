from flask import Flask, request, jsonify
import mysql.connector
import os
from werkzeug.utils import secure_filename


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_attendanceai",
)

cursor = db.cursor()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route("/", methods=["POST"])
def index():
    file = request.files["image"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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
        (`user_id`, `clock_in`, `image_file`, `created_at`, `updated_at`)
        VALUES
        ('{}', '{}', 'http://127.0.0.1:5000/static/uploads/{}', '{}', '{}')
        """.format("102", time, filename, time, time))
        db.commit()
        
        return jsonify({
        "status_code": 200,
        "message": "Success fetching the API",
        "prediction": "joshua",
        "confidence": 100,
        "time": time,
        "attedance_type": attendance_type
    })

@app.route("/clockout", methods=["POST"])
def clock_out():
    id_user = request.form["user_id"]
    time = request.form["time"]
    
    cursor.execute("""
    UPDATE attendances
    SET clock_out='{}', updated_at='{}'
    WHERE user_id='{}'
    """.format(time, time, 102))
    db.commit()
    
    return jsonify({
        "status_code": 200,
        "message": "Success clocking out",
        "time": time
    })


if __name__ == "__main__":
    app.run(
        # host="192.168.1.104"
    )