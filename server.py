import socket

# Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind(('localhost', 12345))

# Enable the server to accept connections (max queue of 1)
server_socket.listen(1)
print("Server is waiting for connection...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    # Receive data from the client (max 1024 bytes at a time)
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client says: {data}")

    # Send a reply to the client
    message = input("Server: ")
    conn.send(message.encode())

# Close the connection
conn.close()
