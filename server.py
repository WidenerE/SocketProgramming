from socket import*
import random
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
#Listen for connections
serverSocket.listen(1)
print('The server is ready to receive')
#Accept connections
connectionSocket, addr = serverSocket.accept()

#Recieve name from client
name = connectionSocket.recv(1024)
print(name.decode() + " has connected!")

#Establish random number bounds
low = 1
high = 100

#generate random number
luckyNum = random.randrange(low, high)

#Main loop
while 1:
        #Send client guess information
        message = "From Server: Number Guessing Game|Number Range: [1,100]|Please Make a Guess: "
        connectionSocket.send(message.encode())

        #Recieve Client response
        recievedMessage = connectionSocket.recv(1024)
        recievedMessage = recievedMessage.decode()
        print(recievedMessage)

        if recievedMessage == "quit":
            break

        #Ensure guess is a number, else throw exception
        try:
            guess = int(recievedMessage)
        except:
            message = "From Server: Number Guessing Game|Number Range: [1,100]|Please Enter a Valid Number"
            connectionSocket.send(message.encode())
            continue
        #Interpret client response and send guess feedback
        if guess == luckyNum:
            message = "From Server: Number Guessing Game|Number Range: [1,100]|You Guessed It!"
            luckyNum = random.randrange(low, high)
        elif guess > high or guess < low:
            message = "From Server: Number Guessing Game|Number Range: [1,100]|Guess Out of Range!"
        elif guess > luckyNum:
            message = "From Server: Number Guessing Game|Number Range: [1,100]|The Number is Less Than " + str(guess)
        elif guess < luckyNum:
            message = "From Server: Number Guessing Game|Number Range: [1,100]|The Number is Greater Than " + str(guess)
			

        connectionSocket.send(message.encode())

connectionSocket.close()
