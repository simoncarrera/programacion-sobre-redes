import socket
import threading
import mysql.connector

db_config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "chat"
}

clientes_conectados = []

def verification_user(usuario, contraseña):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta = "SELECT * FROM users WHERE email = %s"
        cursor.execute(consulta, (usuario,))
        resultado = cursor.fetchone()
        print(resultado)

        cursor.close()
        conexion.close()

        if resultado and resultado[5] == contraseña:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

def manjear_cliente(cliente_socket, cliente_direccion):
    try:
        
        usuario = cliente_socket.recv(1024).decode("utf-8")
        print(f"Usuario recibido: {usuario}")
        
        contraseña = cliente_socket.recv(1024).decode("utf-8")
        print(f"Contraseña recibida: {contraseña}")

        if verification_user(usuario, contraseña):
            cliente_socket.send("Autenticación exitosa.".encode("utf-8"))
            print("exito")
        else:
            cliente_socket.send("Falló la autenticación.".encode("utf-8"))
            cliente_socket.close()
            print("fallo")
            return
        
        clientes_conectados.append(cliente_socket)

        while True:
            opcion = cliente_socket.recv(1024).decode("utf-8")

            if opcion == '1':
                while True:
                    cliente_socket.send("Recibido!".encode("utf-8"))
                    mensaje = cliente_socket.recv(1024).decode("utf-8")
                    print(mensaje)
                    respuesta = f"{usuario}: {mensaje}"
                    for cliente in clientes_conectados:     
                        if cliente != cliente_socket:
                            cliente.send(respuesta.encode("utf-8"))

                

            elif opcion == '2':
                print(f"Desconexión de {cliente_direccion}")
                clientes_conectados.remove(cliente_socket)
                cliente_socket.close()
                break
            else:
                cliente_socket.send("Opción no válida. Intenta de nuevo.\n".encode("utf-8"))
    
    except ConnectionAbortedError:
        print(f"Conexión abortada con {cliente_direccion}")
    except ConnectionResetError:
        print(f"Conexión reiniciada con {cliente_direccion}")
    except Exception as e:
        print(f"Error manejando la conexión con {cliente_direccion}: {e}")
    finally:
        if cliente_socket in clientes_conectados:
            clientes_conectados.remove(cliente_socket)
        cliente_socket.close()

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 65432))
    servidor.listen(5)
    print("Servidor en escucha en el puerto 65432")

    while True:
        cliente_socket, cliente_direccion = servidor.accept()
        print(f"Conexión aceptada de {cliente_direccion}")
        hilo_cliente = threading.Thread(target=manjear_cliente, args=(cliente_socket, cliente_direccion))
        hilo_cliente.start()

if __name__ == "__main__":
    main()