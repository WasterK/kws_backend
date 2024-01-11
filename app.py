from flask import Flask, request, flash, jsonify
from Database_Access import DatabaseAccess

app = Flask(__name__)

databaseURL = "postgres://admin:kRz8psM99PcqnOGLHQaY4GU0UXPs2ldC@dpg-cmco2d6d3nmc73ddamdg-a.singapore-postgres.render.com/kalpwebservice"
db = DatabaseAccess(databaseURL)

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

if __name__ == "__main__":
    app.run(debug=True)
