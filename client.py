import socket

# Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server on localhost and port 12345
client_socket.connect(('localhost', 12345))

while True:
    # Send a message to the server
    message = input("Client: ")
    client_socket.send(message.encode())

    # Receive a reply from the server
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Server says: {data}")

# Close the connection
client_socket.close()
