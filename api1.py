from flask import Flask, jsonify
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        "id": 2,
        "name": "task2",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "task3",
        "description": "This is task 3"
    }
]

tasksJSON = json.dumps(tasks)


@app.route('/')
def home():
    return "Bem-vindo a AC2!!!"


@app.route('/api/tasks')
def get_tasks():
    return tasksJSON


@app.route('/v1/AC2/consultar', methods=["GET"])
def consultar():
    return jsonify(list(range(3))), 200 # Adicionando o código de status 200 OK


if __name__ == '__main__':
    app.run()
