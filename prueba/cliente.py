import socket

def recibir_mensajes(cliente_socket):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode("utf-8")
            if mensaje:
                print(f"\n{mensaje}")
            else:
                break
        except:
            print("Conexión cerrada por el servidor.")
            break

def menu_cliente(cliente_socket):
        print("Menú \n1 Chat con el servidor\n2 Salir.")
        opcion = input("Opción: ")
        cliente_socket.send(opcion.encode("utf-8"))
        
        if opcion == "1":
            while True:
                mensaje = input("mensaje: ")
                cliente_socket.send(mensaje.encode("utf-8"))
                respuesta = cliente_socket.recv(1024).decode("utf-8")
                print("servidor: " + respuesta)
                
        elif opcion == "2":
            print("Desconectando...")
            cliente_socket.close()
        else:
            print("Opción no valida.")             









def main():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente_socket.connect(("localhost", 65432))
        menu_cliente(cliente_socket)
    finally:
        cliente_socket.close()
        
if __name__ == "__main__":
    main()
        