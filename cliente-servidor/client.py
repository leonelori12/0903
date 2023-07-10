import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'  # Dirección IP o nombre de dominio del servidor
port = 12345

client_socket.connect((host, port))

message = '¡Hola, servidor!'
client_socket.sendall(message.encode())

response = client_socket.recv(1024)
print('Respuesta del servidor:', response.decode())

client_socket.close()
