import socket
import selectors


selector = selectors.DefaultSelector()

CONNECTION = ('localhost', 5000)


def get_server_socket(connection):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(connection)
    sock.listen()
    selector.register(fileobj=sock, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(sock):
    client_socket, address = sock.accept()
    print('Connection from', address)
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


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
