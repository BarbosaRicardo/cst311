'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The server receives the data and converts the characters to uppercase. 
The server sends the modified data to the client

'''

# socket module
from socket import *

# initialize variables
serverPort = 12000

# server creates a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# associate server port with TCP socket
serverSocket.bind(('', serverPort))

# wait for client 
serverSocket.listen(1)
print('The server is ready to receive')

# while client is waited on
while True:
   # accepts client and creates new socket (connectionSocket) in the server
   connectionSocket, addr = serverSocket.accept()
   sentence = connectionSocket.recv(1024).decode()
   capitalizedSentence = sentence.upper()
   connectionSocket.send(capitalizedSentence.encode())
   connectionSocket.close()