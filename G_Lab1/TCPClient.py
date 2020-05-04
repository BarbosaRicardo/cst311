'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The client reads a line of chatacters from its keyboard and sends the data to the server 
The client receives the modified data and displays the line on its screen

'''

from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()