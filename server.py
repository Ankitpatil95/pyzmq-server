import zmq


def bind_server():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://0.0.0.0:5555")

    while True:
        msg = input("Enter Message:")
        socket.send(msg.encode('utf-8'))


if __name__ == '__main__':
    bind_server()
