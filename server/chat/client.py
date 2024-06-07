import socket
import threading


HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Conectado al servidor.")
    while True:
        message = input("vos: ")
        s.sendall(message.encode('utf-8'))
    
        s.close()
