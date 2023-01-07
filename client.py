from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
#Connect to Server
clientSocket.connect((serverName,serverPort))
print('Welcome to the Number Guessing Game!')

#Name Prompt
message = input('Please Enter Your Name: ')
clientSocket.send(message.encode())

firstPass = 1

#Guess Loop
while 1:
    if firstPass == 0:
        serverMessage = clientSocket.recv(1024)
        print("\n".join(serverMessage.decode().split("|")))
        serverMessage = clientSocket.recv(1024)
    else:
        serverMessage= clientSocket.recv(1024)
    #Delimit and display server message
    message = input("\n".join(serverMessage.decode().split("|")))
    if message != "quit":
        clientSocket.send(message.encode())
        firstPass = 0
    else:
        clientSocket.send(message.encode())
        break

clientSocket.close()
