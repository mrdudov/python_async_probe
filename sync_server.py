import socket
from select import select

"""
nc localhost 5000
"""

CONNECTION = ('localhost', 5000)

to_monitor = []


def get_server_socket(connection):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(connection)
    server_socket.listen()
    return server_socket


def accept_connsction(in_socket):
    client_socket, address = in_socket.accept()
    print(f'connection from {address}')
    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connsction(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    server_socket = get_server_socket(connection=CONNECTION)
    to_monitor.append(server_socket)
    event_loop()
