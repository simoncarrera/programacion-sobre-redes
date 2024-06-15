import socket
def comando(cliente_socket):
    opcion = input("Que quiere hacer..:")
    if opcion == "/log in":
            usuario = input("usuario: ")
            cliente_socket.send(usuario.encode("utf-8"))
            print("usuario enviado: " + usuario)
            Pass = input("Pass: ")
            cliente_socket.send(Pass.encode("utf-8"))
            print("contraseña enviada: "+ Pass)
            respuesta = cliente_socket.recv(1024).decode("utf-8")
            print("Servidor: " + respuesta)
            
            if respuesta == "Autenticación Exitosa.":
                return True
            else:
                return False
    else:
        print("no valido. Intentelo de nuevo.")

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
        if comando(cliente_socket):
            menu_cliente(cliente_socket)
    finally:
        cliente_socket.close()
        
if __name__ == "__main__":
    main()
        