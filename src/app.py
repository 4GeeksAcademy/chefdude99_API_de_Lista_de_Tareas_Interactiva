from flask import Flask, jsonify
from flask import request

todos = [{'label': 'Mi primera tarea', 'done': False}]

app = Flask(__name__)
@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print('Incoming request with the following body', request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('This is the position to delete:', position)
    todos.pop(position)
    return jsonify(todos)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)