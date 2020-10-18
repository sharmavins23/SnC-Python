from socket import *

# Initialize the socket
serverSocket = socket()

while True:
    # Establish a TCP connection
    connSocket, addr =
    connSocket.settimeout()

    try:
        # Receive data from connSocket
        http_message = connSocket.recv()

        # Parse the message and read the file

        # Make a response
        connSocket.send()

        # Close connection

    except IOError:
        # Handling errors

serverSocket.close()
