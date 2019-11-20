"""
This module will allow client to connect with the server ip and Broadcast Message
"""
import zmq


def bind_server():
    """
    This function binds socket to the ip.
    :return:
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://0.0.0.0:5555")

    while True:
        msg = input("Enter Message:")
        socket.send(msg.encode('utf-8'))


if __name__ == '__main__':
    bind_server()
