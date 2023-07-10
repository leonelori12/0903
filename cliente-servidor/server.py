import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = 'localhost'  
port = 12345

server_socket.bind((host, port))

server_socket.listen(1)

print('El servidor está escuchando en {}:{}'.format(host, port))

while True:
    client_socket, client_address = server_socket.accept()

    print('Se ha establecido una conexión desde {}:{}'.format(client_address[0], client_address[1]))

    data = client_socket.recv(1024)

    if data:
        print('Datos recibidos: {}'.format(data.decode()))

        response = '¡Mensaje recibido correctamente!'
        client_socket.sendall(response.encode())

    client_socket.close()
