from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global `todos`
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        todos.pop(position)  # Eliminar la tarea de la lista de `todos`
        return jsonify(todos), 200  # Retornar la lista actualizada de `todos`
    else:
        return jsonify({"error": "Index out of range"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
