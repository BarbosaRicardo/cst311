'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The client reads a line of chatacters from its keyboard and sends the data to the server 
The client receives the modified data and displays the line on its screen

'''

from socket import *       # allows the creation of sockets 

serverName = 'hostname'    
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

