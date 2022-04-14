from flask import Flask

app = Flask(__name__)


ALL_USERS = [
    {
        'id': 1,
        'name': 'Piotrek',
	    'description': 'Description 1',
	},
	{
		'id': 2,
		'name': 'Witold',
		'description': 'Description 2',
	},
	{
		'id': 3,
		'name': 'Dariusz',
		'description': 'Description 3',
    },
    {
        'id': 4,
        'name': 'Grzegorz',
	    'description': 'Description 4'
    },
]


@app.route('/')
def home_page():
    with open('html/index.html', 'r') as f:
        return f.read()


@app.route('/users')
def get_all_users():
    response = ''
    for user in ALL_USERS:
        response += f'<a href="/user/{user["id"]}"><h1>{user["name"]}</h1></a><p>{user["description"]}</p>'
    return response

@app.route('/user/<int:id>')
def get_user(id: int):
    for user in ALL_USERS:
        if user['id'] == id:
            return f'<h1>{user["name"]}</h1><p>{user["description"]}</p>'
    return '<p style="color:#FF1493;">Його тут нема......</p>'


app.run('localhost', 8000)

