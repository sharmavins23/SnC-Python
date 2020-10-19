from socket import *

# Initialize a socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Get a URI input
HOST = input("Enter the host URI: ")
PORT = int(input("Please enter the port: "))
FILEPATH = input("Please enter the file you want to request from the server: ")

# Establish a TCP connection to the server
clientSocket.connect((HOST, PORT))

# Send HTTP request
clientSocket.send(
    f"GET /{FILEPATH} HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n".encode("utf-8"))

# Receive data from clientSocket
message = clientSocket.recv(1024).decode("utf-8")

# Parse HTTP response
print(message)

# Close the connection
clientSocket.close()
