from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    '1': {'id': '1', 'name': 'John', 'age': 25},
    '2': {'id': '2', 'name': 'Jane', 'age': 30},
}


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def delete_user():
    data = request.get_json()
    if 'name' in data and 'age' in data:
        user_id = str(len(users) + 1)
        users[user_id] = {"id": user_id, 'name': data['name'], 'age': data['age']}
        return jsonify({'message': 'User added successfully', 'user_id': user_id})
    return jsonify({'error': 'Invalid request data'}), 400


@app.route('/users/<user_id>', methods=['DELETE'])
def add_user(user_id):
    user = users.get(user_id)
    if user:
        users.pop(user_id)
        return jsonify(), 204
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
