'''
Ricardo Barbosa 
Date: May 3, 2020
Class: CST 311 
Description: The client reads a line of chatacters from its keyboard and sends the data to the server 
The client receives the modified data and displays the line on its screen

'''

# socket module
from socket import *

# initialize variables
serverName = '127.0.0.1'
serverPort = 12000

# create client socket; IPv4/TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# initiate TCP connection between client and server
clientSocket.connect((serverName, serverPort))

# receive user input until carriage return
sentence = input('Input lowercase sentence: ')

# user input sent through client's socket, into TCP connection
clientSocket.send(sentence.encode())

# user input on server side is combined until received in full
modifiedSentence = clientSocket.recv(1024)

# user input prints 
print('From Server: ', modifiedSentence.decode())

# socket and TCP connection close between client and server
clientSocket.close()