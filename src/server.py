from socket import *
from os import path

HOST = "127.0.0.1"  # Localhost
PORT = 9999  # Development port
# NOTE: On my machine, port 8080 does not work
# OSError: [WinError 10013] An attempt was made to access a socket in a way
#  forbidden by its access permissions
# This server has been tested to work properly on port 9999. It seems to be an
#  issue with firewall setup, but the server works properly circumventing that

# Create path for HTML file loading
THIS_FOLDER = path.dirname(path.abspath(__file__))

# Initialize the socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))  # Bind to IP addr. and port
serverSocket.listen()  # Wait for requests

print("Server is online and awaiting requests.")

while True:
    # Establish a TCP connection
    connSocket, addr = serverSocket.accept()
    print("Connected to", addr)
    connSocket.settimeout(1000)

    try:
        # Receive data from connSocket
        http_message = connSocket.recv(1024).decode("utf-8")

        # Parse the message and read the file
        http_message_list = http_message.split(" ")  # Split across whitespace
        method = http_message_list[0]  # First string is method
        request_filepath = http_message_list[1]  # Next is requested file
        print(http_message)  # Log the connection request

        print("Client request:", request_filepath)

        # Make a response
        # If not a GET request, or not on server...
        if (method != "GET" or request_filepath != "/index.html"):
            # Write the error 404 response header
            header = "HTTP/1.1 404 Not Found\n\n"

            # Load the error 404 HTML response file
            fileToSend = path.join(THIS_FOLDER, "filenotfound.html")
        else:  # Valid HTTP response (currently only supports GET to index.html)
            # Write the response header
            header = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"

            # Load the HTML response file
            fileToSend = path.join(THIS_FOLDER, "index.html")

        # Finally, append and send back the file
        sentFile = open(fileToSend, "rb")  # Read as bytes
        file_response = sentFile.read()  # Read the file
        sentFile.close()  # Close the file
        response = header.encode("utf-8")  # Encode the header
        response += file_response  # Add the read file bytestream

        connSocket.send(response)  # Send our response

        # Close connection
        connSocket.close()
    except IOError as e:
        print("An error has occurred!", e)

serverSocket.close()
