import socket

server_host = "127.0.0.1"
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_host, server_port))
print("Conetado.")

while True:
    message = input("vos: ")
    client_socket.sendall(message.encode("utf-8"))
    
    
client_socket.close()