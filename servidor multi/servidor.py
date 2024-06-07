import socket 
import threading
import _mysql_connector


db_config = {
    "users":" ",
    "password": " ",
    "host" : "localhost",
    "database" : "chat"
}

def verification_user(usuario, contraseña):
    try:
        conexion = _mysql_connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta = "SELECT pass FROM users WHERE users = %s"
        cursor.execute(consulta, (usuario,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado and resultado[0] == contraseña:
            return True
        else:
            return False
    except _mysql_connector.Error as err:
        print(f"Error: {err}")
        return False
    
def manjear_cliente(cliente_socket, cliente_direccion):
    cliente_socket.send("Usuario: ".encode("utf-8"))
    usuario = cliente_socket.recv(1024).decode("utf-8")
    cliente_socket.send("Contraseña: ".encode("utf-8"))
    contraseña = cliente_socket.recv(1024).decode("utf_8")

    if verification_user(usuario, contraseña):
        cliente_socket.send("Autentucación exitosa. \n".encode("utf-8"))
    else:
        cliente_socket.send("Falló la autenticación\n".encode("utf-8"))
        cliente_socket.close()
        return
    while True:
        cliente_socket.send("Menú:\n1. Chat con el servidor\n0pción: ".encode("utf-8"))
        mensaje = cliente_socket.recv(1024).decode("utf-8")
        respuesta = f"Servidor: {mensaje}"
        cliente_socket.send(respuesta.encode("utf-8"))
    else:
        cliente_socket.send("Opción no válida. Intenta de nuevo. \n".encode("utf-8")) 

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 12345))
    servidor.listen(5)
    print("servidor en escucha en el puerto 123456")

    while True:
        cliente_socket, cliente_direccion = servidor.accept()
        print(f"Conexion aceptada de {cliente_direccion}")
        hilo_cliente = threading.Thread(target = manjear_cliente, args = (cliente_socket, cliente_direccion))
        hilo_cliente.start()

if __name__ == "__main__":
    main()