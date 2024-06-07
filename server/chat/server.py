import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Cliente dice {data}") 
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f"escuchando en el puerto {PORT} en la IP {HOST}")
    s.listen(3)
    print ("servidor escuchando en {}:{}...".format(HOST, PORT))
    
while True:
    conn, addr = s.accept()
    print(f"Cliente conectado desde:  {addr} ")
    client_handler = threading.Thread(target=handle_client, args=(s,))
    client_handler.start()
