# Program Name: Python Multi-Client Chat Application

# Purpose:
# To allow multiple users to connect to a chat room and exchange messages in real time.

# How it Works:

# Server (server.py):

# Starts and listens on 127.0.0.1 port 5555.

# Waits for incoming client connections.

# Asks each new client for a nickname.

# Stores connected clients and their nicknames.

# Sends ("broadcasts") messages from one client to all others.

# Client (client.py):

# Connects to the server.

# Sends nickname when requested.

# Can send messages to the server.

# Receives messages from other clients via the server.

# What the Output Shows:

# The server terminal confirms connections with nicknames “kashish” and “ram”.

# The client terminals show when someone joins the chat.

# “Connected to the server!” confirms successful connection.

# Why This Works:

# Uses threading so the server can handle multiple clients at the same time.

# Messages are sent using broadcast() so all connected clients receive updates.

# Possible Real-World Uses:

# Group chats, multiplayer games, team collaboration tools.
