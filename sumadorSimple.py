#!/usr/bin/python

#  P2: Ejercicio 14.5 Sumador Simple
#  Rosa Cristina Ruiz Rivas

import socket

# Crea un socket sobre TCP y se conecta a un determinado puerto.
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(("localhost",1234))

# Podra escuchar hasta 5 conexiones TCP.
mySocket.listen(5)

# primero nos indica que la URL nos proporciona el primer sumando.
# Inicializamos sumando.
primero = True
sumando = 0 

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP Request received:'    
        datos = recvSocket.recv(1024)
        print datos
        listaDatos = datos.split()
        # Si introducimos el segundo sumando se lo suma al primero
        sumando += int(listaDatos[1].split("/")[1])
        if primero:
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + 
                            "<html><body><p>Introduzca el segundo sumando:</p>" +
                            "</body></html>" + "\r\n")
        else:
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>La suma es:" + str(sumando) +
                             "</h1></body></html>" + "\r\n")
            # Ya se ha sumado el primer y segundo sumando 
            sumando = 0           
        primero = not primero
        recvSocket.close()
except ValueError:
    print "Introduzca numero a sumar"  
    recvSocket.send("HTTP/1.1 400 Bad request\r\n\r\n" +
                    "<html><body><h1>400 Solicitud incorrecta!</h1>" + 
                    "</body></html>" + "\r\n")            
except KeyboardInterrupt:
    mySocket.close()
  
