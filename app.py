
from flask import Flask, jsonify, request
import csv

app = Flask(__name__)



# Helper function to read user data from CSV
def read_user_data():
    users = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users

# Helper function to write user data to CSV
def write_user_data(users):
    fieldnames = ['id', 'name']
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

@app.route('/v1/users', methods=['GET'])
def get_users():
    users = read_user_data()
    return jsonify(users)

###########################################
#@app.route('/v1/users', methods=['POST'])
#
#def create_user():
#    users = read_user_data()
#    user = {
#        'id': int(request.json['id']),
#        'name': request.json['name']
#    }
#    users.append(user)
#    write_user_data(users)
#    return jsonify(user)
##########################################
@app.route('/v1/users', methods=['POST'])
def create_user():
    users = read_user_data()

    if not request.is_json:
        return jsonify({'message': 'Invalid request'}), 400

    user_id = request.json.get('id')
    name = request.json.get('name')

    if not user_id or not name:
        return jsonify({'message': 'Missing user_id or name'}), 400

    user = {
        'id': int(user_id),
        'name': name
    }

    users.append(user)
    write_user_data(users)

    return jsonify(user), 201


@app.route('/v1/users/<int:userId>', methods=['GET'])
def get_user(userId):
    users = read_user_data()
    for user in users:
        if user['id'] == str(userId):
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')

