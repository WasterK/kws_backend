from flask import Flask, request, flash, jsonify
from flask.views import MethodView
from Database_Access import DatabaseAccess
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    return jsonify({"msg": "Login failed. Check your credentials and try again.", "status": "fail"}), 401
    
@app.route('/get-cable-info/<int:deviceId>', methods=['GET'])
def get_cable_info(deviceId):
    try:
        cableInfo = db.get_all_cable_info(deviceId=deviceId)
        return jsonify({"device Id": deviceId, "cable info": cableInfo}), 200
    except Exception as e:
        return jsonify({"device Id": deviceId, "cable info": f"somthing went wrong: {e}"}), 404
    
@app.route("/get-all-devices", methods=["GET"])
def get_all_device():
    deviceId = db.get_all_devices()
    return jsonify({"device ids" : deviceId})

if __name__ == "__main__":
    app.run(debug=True)
