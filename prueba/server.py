import socket 



def mensaje_cliente(cliente_socket):
    
    while True:
        opcion = cliente_socket.recv(1024).decode("utf-8")
        print("opcion Recibida")
            
        if not opcion:
            print("no valido")
            break
        print("Cliente: " + opcion)

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("127.0.0.1", 65432))
    servidor.listen(5)
    print("Servidor en escucha en 65432")
    while True:
        servidor.accept()
        print("Conexion aceptada")
        
        
    

    
if __name__ == "__main__":
    main()
    
    
    