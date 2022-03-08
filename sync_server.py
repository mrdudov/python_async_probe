import socket

"""
nc localhost 5000
"""

HOST = 'localhost'
PORT = 5000


def get_server_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()
    return server_socket


server_socket = get_server_socket(host=HOST, port=PORT)

while True:
    print('Before accept()')
    client_socket, address = server_socket.accept()
    print(f'Connection from {address}')

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
    
    print('outside inner while True loop')
    client_socket.close()
