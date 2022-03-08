import socket
import selectors

"""
nc localhost 5000
"""

CONNECTION = ('localhost', 5000)

selector = selectors.DefaultSelector()


def get_server_socket(connection):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(connection)
    server_socket.listen()
    selector.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ,
        data=accept_connsction
    )


def accept_connsction(in_socket):
    client_socket, address = in_socket.accept()
    print(f'connection from {address}')
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    get_server_socket(connection=CONNECTION)
    event_loop()
