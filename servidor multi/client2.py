import socket
import threading

def autenticar_cliente(cliente_socket):
    print("log in")
    usuario = input("Email: ")
    cliente_socket.send(usuario.encode("utf-8"))
    print("email recibido: " + usuario)
    contraseña = input("Contraseña: ")
    cliente_socket.send(contraseña.encode("utf-8"))
    print("contraseña recibida: " + contraseña)
    
    respuesta = cliente_socket.recv(1024).decode("utf-8")
    print("respuesta del servidor: "+ respuesta)
    
    if respuesta.strip() == "Autenticación exitosa.":
        return True    
    else:
        return False
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
    while True:
        print("Menú:\n1. Chat con el servidor\n2. Salir")
        opcion = input("Opción: ")
        cliente_socket.send(opcion.encode("utf-8"))
        
        if opcion == "1":
            threading_recibir = threading.Thread(target = recibir_mensajes, args=(cliente_socket,))
            while True:
                mensaje = input("Escribe tu mensaje: ")
                cliente_socket.send(mensaje.encode("utf-8"))
                respuesta = cliente_socket.recv(1024).decode("utf-8")
                print("servidor: "+ respuesta)
            
        elif opcion == "2":
            print("Desconectando...")
            cliente_socket.close()
            break
        else:
            print("Opción no válida. Intente otra vez.")

        respuesta_servidor = cliente_socket.recv(1024).decode("utf-8")
        print(f"Respuesta del servidor: {respuesta_servidor}")

def main():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente_socket.connect(("localhost", 65432))       
        if autenticar_cliente(cliente_socket):
            menu_cliente(cliente_socket)
        else:
            print("Autenticación fallida.")
            cliente_socket.close()
    
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cliente_socket.close()

if __name__ == "__main__":
    main()