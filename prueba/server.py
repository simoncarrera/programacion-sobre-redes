import socket 

clientes = ["simon", "massi," "pela", "crespo"]

Passw = ["12", "32", "54", "65"]

def verificar_cliente(usuario,Pass):
        print("entro")
        for usuario in clientes:
            print("entro2")
            if usuario == clientes:
               for Pass in Passw:
                   print("entro3")
                   if Pass == Passw:
                       return True
                   else:
                       return False
                   
                   
def datos_usuario(cliente_socket):
        usuario = cliente_socket.recv(1024).decode("utf-8")
        print(f"usuario recibido: {usuario}")
        Pass = cliente_socket.recv(1024).decode("utf-8")
        print(f"contraseña recibida: {Pass}")
        
        if verificar_cliente(usuario, Pass):
            cliente_socket.send("Autenticacion exitosa.".encode("utf-8"))
            print("exito")
        else:
            cliente_socket.send("Autenticacion Fallida.".encode("utf-8"))
            cliente_socket.close()
            return
        
        
        while True:
            opcion = cliente_socket.recv(1024).decode("utf-8")
            print("opcion Recibida")
                
            if opcion == "1":
                while True:
                    cliente_socket.send("Recibido!".encode("utf-8"))
                    mensaje = cliente_socket.recv(1024).deocde("utf-8")
                    print(mensaje)
            elif opcion =="2":
                print("Cerrando conexión...")
                cliente_socket.close()
                break
            else:
                print("No valido.")
    
        
    
    
                    

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("127.0.0.1", 65432))
    servidor.listen(5)
    print("Servidor en escucha en 65432")
    while True:
        cliente_socket = servidor.accept()
        print(f"Conexion aceptada con: {cliente_socket}")
         
if __name__ == "__main__":
    main()
    
    
    