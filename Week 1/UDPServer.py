'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The server receives the data and converts the characters to uppercase. 
The server sends the modified data to the client

'''

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
   message, clientAddress = serverSocket.recvfrom(2048)
   modifiedMessage = message.decode().upper()
   serverSocket.sendto(modifiedMessage.encode(), clientAddress)
   