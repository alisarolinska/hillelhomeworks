import flask
from flask import Flask, request

app = Flask(__name__)
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


@app.route('/users')
def get_users():
	return flask.jsonify(users)


@app.route('/user', methods=['POST'])
def create_user():
	data = request.json
	if 'name' in data and 'last name' in data and 'password' in data and 'email' in data:
		email = data['email']
		if len(list(filter(lambda x: x['email'] == email, users))) != 0:
			return flask.jsonify({
					'code': 2,
					'message': 'Пользователь уже есть в системе'
			})
		users.append(data)
		return flask.jsonify({
			'code': 0,
			'message': 'Пользователь создан'
		})
	return flask.jsonify({
			'code': 1,
			'message': 'У пользователя есть обязательные поля: username, password, email'
	})


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user():
	return flask.jsonify(users)


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
	global users
	if len(users) >= user_id:
		users.pop(user_id - 1)
		return flask.jsonify({
			'code': 0,
			'message': 'Пользователь удален!'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'Пользователь не найден!'
		})


if __name__ == '__main__':
	app.run(debug=True)