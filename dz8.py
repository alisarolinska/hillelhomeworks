import flask
from flask import request

app = flask.Flask(__name__)

tasks = []


from pydantic import BaseModel, ValidationError, validator
from datetime import datetime


class Task(BaseModel):
	id: int
	name: str
	description: str
	deadline: str
	created_at: datetime = datetime.now()


@validator('name')
def name_length(cls, n):
    if len(n) < 2 or len(n) > 20:
        raise ValueError('название должно содержать от 2 до 10 символов')
    return n


@validator('deadline')
def validate_email(cls, b):
    if '.' not in b:
        raise ValueError('Некорректная запись даты выполнения')
    return b


@validator('description')
def desc_length(cls, v):
    if len(v) < 2 or len(v) > 200:
        raise ValueError('описание должно содержать от 2 до 10 символов')
    return v


try:
    task_1 = Task(name ='уборка', description ='убрать квартиру', deadline='31.02.2038')
    print(task_1)
    print(task_1.json())
    print(task_1.dict())
except ValidationError as e:
	print(e.errors())
	print(e.json())



@app.route('/')
def index():
	return 'OK!'


@app.route('/task', methods=['GET'])
def get_task():
	return flask.jsonify(tasks)


@app.route('/task/<int:user_id>', methods=['DELETE'])
def delete_task(task_id: int):
	global tasks
	if len(tasks) >= task_id:
		tasks.pop(task_id - 1)
		return flask.jsonify({
			'code': 0,
			'message': 'Task deleted!'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'Task not found!'
		})


@app.route('/task', methods=['POST'])
def create_task():
        data = request.json
        if 'id' in data and 'name' in data and 'description' in data and 'deadline' in data:
            name = data['name']
            if len(list(filter(lambda x: x['name'] == name, tasks))) != 0:
                return flask.jsonify({
                    'code': 2,
                    'message': 'задание уже создано'
                })
            tasks.append(data)
            return flask.jsonify({
                'code': 0,
                'message': 'Task created'
            })
        return flask.jsonify({
            'code': 1,
            'message': 'У задания есть обязательные поля: название, описание, выполнить до'
        })

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_task(task_id: int):
    global tasks
    data = request.json
    if len(tasks) >= task_id:
        if 'name' in data and 'description' in data and 'deadline' in data:
            tasks[task_id - 1] = data
            return flask.jsonify({
                'code': 0,
                'message': 'Task updated!'
            })
        return flask.jsonify({
            'code': 1,
            'message': 'У задания есть обязательные поля: название, описание, выполнить до'
        })
    return flask.jsonify({
        'code': 3,
        'message': 'Task not found!'
    })


if __name__ == '__main__':
    app.run('localhost', 6000)
    app.run(debug=True)



