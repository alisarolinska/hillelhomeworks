import flask
from flask import request

app = flask.Flask(__name__)
users = [
    {
        'id': 1,
        'name': 'Piotrek',
		'last name': 'Pietrenko',
		'email': '1@poczta',
		'password': '1111'
		,
	},
	{
		'id': 2,
		'name': 'Witold',
		'last name': 'Kozhuszenko',
		'email': '2@poczta',
		'password': '2222'
		,
	},
	{
		'id': 3,
		'name': 'Dariusz',
		'last name': 'Brzyza',
		'email': '3@poczta',
		'password': '3333'
		,
    },
    {
        'id': 4,
        'name': 'Grzegorz',
		'last name': 'Brzenczyszczykiewicz',
		'email': '4@poczta',
		'password': '4444'
    },
]


@app.route('/')
def index():
	return 'OK!'


@app.route('/users')
def get_users():
	return flask.jsonify(users)


@app.route('/user', methods=['POST'])
def create_user():
	global users
	user_data = request.json
	user_data['id'] = len(users) + 1
	users.append(user_data)
	return flask.jsonify(user_data)


@app.route('/task/<int:task_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
	global users
	filtered_users = list(filter(lambda x: x['id'] == user_id, users))
	if len(filtered_users) == 0:
		return {'message': 'Пользователь не найден!'}, 404
	if request.method == 'GET':
		return flask.jsonify(filtered_users[0])
	elif request.method == 'DELETE':
		users = list(filter(lambda x: x['id'] != user_id, users))
		return {'message': 'Пользователь удален!'}


if __name__ == '__dz7__':
	app.run(debug=True)