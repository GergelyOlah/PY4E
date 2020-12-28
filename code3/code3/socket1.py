import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket is like a file-handle.
mysock.connect(('data.pr4e.org', 80)) #Functiion call with a tuple as parameter (domain name/destination, PORT)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
