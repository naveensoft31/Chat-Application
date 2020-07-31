#import modules
import socket
import sys
import time

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                          #Get the hostname of your device

print(" server will start on host : ", host)

port = 8080                                  #Give the port number
sckt.bind((host,port))                        #Bind the socket with host and port

print(" Server done binding to host and port successfully")
print("Server is waiting for incoming connections")

sckt.listen(1)
conn, addr = sckt.accept()

print(addr, "  connected to the server and is now online ...")

while 1:
            message = input(str(">> "))      #give input of your message
            message = message.encode()
            conn.send(message)               #message can be send
            print("message has been sent...")
            print("")
            incoming_message = conn.recv(8080)           #connect to incoming message
            incoming_message = incoming_message.decode()
            print(" Client : ", incoming_message)
            print("")
