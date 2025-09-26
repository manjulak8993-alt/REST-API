from flask import Flask, request, jsonify
app = Flask(__name__)
users = {}
uid = 1
@app.route('/users', methods=['GET', 'POST'])
def users_route():
    global uid
    if request.method == 'GET':
        return jsonify(users)
    data = request.json
    if not data or "name" not in data:
        return {"error": "Name is required"}, 400
    users[uid] = {"id": uid, "name": data["name"]}
    uid += 1
    return jsonify(users[uid - 1]), 201
@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_route(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404
    if request.method == 'GET':
        return jsonify(users[user_id])
    if request.method == 'PUT':
        users[user_id]["name"] = request.json.get("name", users[user_id]["name"])
        return jsonify(users[user_id])
    return jsonify(users.pop(user_id))  
if __name__ == "__main__":
    app.run(debug=True)