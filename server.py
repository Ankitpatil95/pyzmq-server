"""
This module will allow client to connect with the server ip and Broadcast Message
"""
import zmq
from flask import Flask, render_template, request

app = Flask(__name__)

context = zmq.Context()
zmq_socket = context.socket(zmq.PUB)


@app.route('/')
def index():
    """
    This functions redirect to home.
    :return:
    """
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def bind_server():
    """
    This function binds socket to the ip.
    :return:
    """
    try:
        zmq_socket.bind("tcp://0.0.0.0:5555")
        return render_template('send_message.html')

    except Exception as e:
        return render_template('send_message.html')


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
        return render_template('send_message.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
