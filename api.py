from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
app.config["Debug"] = True

users_dict =[]

@app.route('/users', methods =['GET'])
def get_users_id():
    users = []
    for user in users_dict:
        contProp = 0
        for arg in request.args:
            val = user[arg]
            param = request.args[arg]
            if isinstance(val,int):
                param = int(param)
            if isinstance(val, str):
                val = val.upper()
                param = param.upper()
            if val == param:
                contProp += 1
        if contProp == len(request.args):
            users.append(user)
    return jsonify(users)
    # if 'id' in request.args:
    #     id = int(request.args['id'])
    # else:
    #     return "Erro: Id Não identificado, por favor inserir id válido"
    
    # for user in users_dict:
    #     if user['id'] == id:
    #         return jsonify(user)
    # return{}

@app.route('/users/<id>', methods =['GET'])
def get_user_id_in_path(id):
    for user in users_dict:
        if user ['id'] == int(id):
            return jsonify(user)
    return{}

@app.route('/user', methods=['POST'])
def post_users():
    user = request.get_json()
    user['id'] = len(users_dict) + 1
    users_dict.append(user)
    return jsonify(user)

@app.route('/user', methods = ['PUT'])
def put_users():
    user = request.get_json()
    for i, u in enumerate(users_dict):
        if u['id'] == user['id']:
            users_dict[i] = user
    return{}

@app.route('/user/<id>', methods=['DELETE'])
def delete_users(id):
    for user in users_dict:
        if user ['id'] == int(id):
            users_dict.remove(user)
    return{}

if __name__ == '__main__':
    app.run()