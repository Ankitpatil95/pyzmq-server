"""
This module will allow client to connect with the server ip and Broadcast Message
"""
import zmq
from flask import request, json
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from models import app, db, User

context = zmq.Context()
zmq_socket = context.socket(zmq.PUB)


def authenticate(username, password):
    req_dict = request.get_json()
    user = User.query.filter_by(username=req_dict.get('username')).first()
    password = req_dict.get('password')
    if user and safe_str_cmp(user.hash_password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    print(user_id)
    return User.query.filter_by(id=user_id).first()


jwt = JWT(app, authenticate, identity)


@app.route('/')
@jwt_required()
def index():
    """
    This functions redirect to home.
    :return:
    """
    return "Home"


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        request_dict = request.get_json()
        user = User(username=request_dict.get('username'), email=request_dict.get('email'),
                    hash_password=request_dict.get('password'))
        db.session.add(user)
        db.session.commit()
        user_dict = {"username": user.username, "message": "User created successfully"}
        response = app.response_class(
            response=json.dumps(user_dict),
            status=200,
            mimetype='application/json'
        )
        db.session.remove()
        return response
    else:
        pass


@app.route('/create', methods=['POST'])
def bind_server():
    """
    This function binds socket to the ip.
    :return:
    """
    try:
        zmq_socket.bind("tcp://0.0.0.0:5555")
        return "render_template('send_message.html')"

    except Exception as e:
        return "render_template('send_message.html')"


@app.route('/send', methods=['GET', 'POST'])
def send_message():
    """
    This function use to send message to connected clients.
    :return:
    """
    if request.method == "POST":
        msg = request.form['comment']
        zmq_socket.send(msg.encode('utf-8'))
        return "Message sent successfully."
    else:
        return "render_template('send_message.html')"


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
