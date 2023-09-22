from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["Debug"] = True

# users_dict = [{"id":"1", "Nome":"jose"},{"id":"2","Nome":"Rafael"}]
# users_dict = [{"id": "1", "Nome": "jose"}, {"id": "2", "Nome": "Rafael"}]
users_dict = [{"id": "1", "nome": "jose"}, {"id": "2", "nome": "Rafael"}]

@app.route('/users', methods=['GET'])
def get_users_id():
    users = []
    for user in users_dict:
        contProp = 0
        for arg in request.args:
            val = user[arg]
            param = request.args[arg]
            if isinstance(val, int):
                param = int(param)
            if isinstance(val, str):
                val = val.upper()
                param = param.upper()
            if val == param:
                contProp += 1
        if contProp == len(request.args):
            users.append(user)
    
    users_with_names = [{'id': user['id'], 'nome': user['nome']} for user in users]
    return jsonify(users_with_names)

@app.route('/users/<id>', methods=['GET'])
def get_user_id_in_path(id):
    for user in users_dict:
        if user['id'] == id:
            
            return jsonify(user)
    return '', 404

@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    user['id'] = str(len(users_dict) + 1)
    users_dict.append(user)
    return jsonify(user), 201

# @app.route('/user', methods=['PUT'])
# def put_users():
#     user = request.get_json()
#     for i, u in enumerate(users_dict):
#         if u['id'] == user['id']:
#             users_dict[i] = user
#             return '', 204
#     return '', 404
@app.route('/user', methods=['PUT'])
def put_users():
    user_data = request.get_json()  
    for user in users_dict:
        if user['id'] == user_data['id']:
            user['nome'] = user_data['nome']  
            return '', 204  
    return '', 404  


@app.route('/user/<id>', methods=['DELETE'])
def delete_users(id):
    for user in users_dict:
        if user['id'] == id:
            users_dict.remove(user)
            return '', 204
    return '', 404

if __name__ == '__main__':
    app.run()
