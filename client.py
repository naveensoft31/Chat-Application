#import modules
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input(str("Please enter the hostname of the server : "))    #enter the hostname of the server side
port = 8080                                                        #Give the port number
s.connect((host,port))                                             #connect the socket with host and port
print(" Connected to chat server")
while 1:
            incoming_message = s.recv(1024)                         #Recieve the server sended message
            incoming_message = incoming_message.decode()
            print(" Server : ", incoming_message)
            print("")
            message = input(str(">> "))                              #enter the message send to server 
            message = message.encode()
            s.send(message)                                           #Message can be sended
            print("message has been sent...")
            print("")
