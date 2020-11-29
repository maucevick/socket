import socket

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind(("127.0.0.1", 9000))
ser.listen(1)
print("Servidor Prueba")
cli, addr = ser.accept()
if cli > 0:
	print ("Cliente Conectado")
while True:

    recibido = cli.recv(1024)
    #Mensaje Cliente Conectado 
    print "Cliente: " + str(addr[0]) + " Puerto: " + str(addr[1])
    #Devolvemos el mensaje al cliente
    cli.send("Hola Soy El Servidor")

#Cerrar cliente y servidor
cli.close()
print("Cliente Desconectado")
ser.close()
print ("Conexiones Cerradas")
