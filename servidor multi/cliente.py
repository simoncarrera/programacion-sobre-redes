import socket

def aunteticar_cliente(cliente_socket):
    usuario = input("Usuario: ")
    cliente_socket.send(usuario.encode("utf-8"))
    contraseña = input("Contraseña: ")
    cliente_socket.send(contraseña.encode("utf-8"))
    
    respuesta = cliente_socket.recv(1024).decode("utf-8")
    print(respuesta)
    
    if "Autentucación exitosa." in respuesta:
        return True
    else:
        return False
    
def menu_cliente(cliente_socket):
    while True:
        print("Menú: \n1. Chat con el servidor \n2. Salir")
        opcion = input("Opción: ")
        cliente_socket.send(opcion.encode("utf-8"))
        
        if opcion == "1":
            mensaje = input("Escribe tu mensaje: ")
            cliente_socket.send(mensaje.encode("utf-8"))
            respuesta = cliente_socket.recv(1024).decode("utf-8")
            print(respuesta)
        elif opcion == "2":
            print("desconectando...")
            cliente_socket.close()
            break
        else: 
            print("Ocpion no valida. Intente otra vez.")
            

         
    