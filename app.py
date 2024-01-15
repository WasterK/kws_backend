from flask import Flask, request, flash, jsonify
from Database_Access import DatabaseAccess

app = Flask(__name__)

databaseURL = "postgres://admin:kRz8psM99PcqnOGLHQaY4GU0UXPs2ldC@dpg-cmco2d6d3nmc73ddamdg-a.singapore-postgres.render.com/kalpwebservice"
db = DatabaseAccess(databaseURL)

@app.route("/", methods = ['GET'])
def default():
    return "KWS welcomes you"

# Sample route for user login``
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if db.user_validation(username=username,password=password):
        return jsonify({'msg': "Login successful!", "status": "success"}), 200
    else:
        return jsonify({"msg": "Login failed. Check your credentials and try again.", "status": "fail"}), 401
    
@app.route('/get-cable-info/<int:deviceId>', methods=['GET'])
def get_cable_info(deviceId):
    try:
        cableInfo = db.get_all_cable_info(deviceId=deviceId)
        return jsonify({"device Id": deviceId, "cable info": cableInfo}), 200
    except Exception as e:
        return jsonify({"device Id": deviceId, "cable info": "somthing went wrong"}), 404

if __name__ == "__main__":
    app.run(debug=True)
