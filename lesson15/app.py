from flask import Flask  , jsonify , request

app = Flask(__name__)

users = [
    {"id" : 1001, "name" : "mina" , "age" : 30},
    {"id" : 1002, "name" : "ali" , "age" : 20},
    {"id" : 1003, "name" : "sara" , "age" : 40}
]

@app.route("/api/users" , methods= ['GET'])
def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>" , methods= ['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id :
            return jsonify(user)
    return jsonify({"message" : "user not found"}) , 404


@app.route("/api/users" , methods = ['PUT'])
def insert_user ():
    data = request.get_json()
    new_user = {
        "id" : len(users) + 1000,
        "name" : data.get("name") , 
        "age" : data.get("age")
    }
    users.append(new_user)
    return jsonify(new_user)


@app.route("/api/users/<int:user_id>" , methods = ['POST'])
def edit_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id :
            user['name'] = data.get("name")
            user['age'] = data.get("age")
            return jsonify(user)
    return jsonify({"message" : "user not found"}) , 404


@app.route("/api/users/<int:user_id>" , methods = ['DELETE'])
def delete_user(user_id) :
    global users
    users = [ user for user in users if user["id"] != user_id]
    return jsonify({"message" : "user deleted"}) , 200

@app.route("/")
def home() :
    return "welcome to my first api"

if __name__ == "__main__" :
    app.run(debug=True)