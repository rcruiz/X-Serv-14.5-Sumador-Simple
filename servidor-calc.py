#!/usr/bin/python3

import socket
import calculadora

# Crea un socket sobre TCP y se conecta a un determinado puerto.
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

# Podra escuchar hasta 5 conexiones TCP.
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP Request received:')
        datos = recvSocket.recv(1024).decode()
        print(datos)
        recurso = datos.split()[1]
        # Extraemos los datos de la operación
        try:
            _, op1, operacion, op2 = recurso.split("/")
            op1, op2 = float(op1), float(op2)
            # Llamamos a calculadora
            res = calculadora.funciones[operacion](op1, op2)
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><p>El resultado es: " + str(res) +
                            "</p></body></html>\r\n", 'utf-8'))
        except (ValueError, KeyError):
            recvSocket.send(bytes("HTTP/1.1 400 Bad request\r\n\r\n" +
                            "<html><body><h1>400 Solicitud incorrecta!</h1>" +
                            "</body></html>" + "\r\n", 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
