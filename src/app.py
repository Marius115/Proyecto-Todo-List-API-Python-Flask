
from flask import Flask, jsonify
from flask import request
import json


app = Flask(__name__)

todos = [{ "label": "My first tasker", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    print("This is the position to delete: ",position)
    new_todos = []
    for i in range(len(todos)):
        if i != position:
            new_todos.append(todos[i])
    todos = new_todos
    return jsonify(todos)







#end of the line
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)



  