import socket
import time as t
import threading as th

"""
Originally more complicated, server would dynamically connect and manage clients
Now 2 clients only are required for LAN game, they must be connected which means server and client code doesn't need to be designed to bend their backs to keep clients connected and communicating at the same time
"""

# Main
print("\033[0;33mStarting server\033[0;33m")

Port = 12345 # default port for socket
# Creates server socket
try: 
    # Socket creation
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    print("\033[0;32mSocket successfully created\033[0;32m")
    # Prepares socket for connections
    ServerSocket.bind(("", Port)) # Binds socket to address at port, empty address means server listens for all network
    print(f"\033[0;33mSocket binded at port {Port}\033[0;33m")
    ServerSocket.listen(2) # Listens for incoming connections, backlog is 2 meaning max connections
    print("\033[0;33mListening for incomming connections\033[0;33m")
except socket.error: 
    print(f"\033[0;31mERROR : socket creation failed : {socket.error}\033[0;31m")
    quit()

# Connects 2 clients together
Clients = []
while len(Clients) < 2:
    try:
        # Accepts clients and records them
        ClientSocket, Address = ServerSocket.accept()
        ClientSocket.send(f"ClientNumber:{len(Clients) + 1}".encode("utf-8"))
        Clients.append([ClientSocket, Address])
        print(f"\033[0;32mGot connection from {Address}\033[0;32m")
    except Exception:
        print(f"\033[0;31mERROR : Cannot accept to client{Exception}\033[0;31m")

# While both clients connected, continues to sync game data
ClientConnected = 2
while ClientConnected == 2:
    # Every second, polls to check clients are connected and syncs game data
    if (t.time() % 1) == 0:
        try:
            # Goes through both clients
            for Client in Clients:
                # Checks client is connected
                ClientData = Client[0].recv(2048).decode("utf-8")
                if (ClientData == b"") or (ClientData == ""):
                    ClientConnected -= 1
                    break
                # Syncs data with that client
                else:
                    print(ClientData)
                    Client[0].send(f"Hello client {Clients.index(Client) + 1}".encode("utf-8"))
        except Exception:
            print(f"\033[0;31mERROR : {Exception}\033[0;31m")
            ClientConnected -= 1
            break

# Closes socket and program
print("\033[0;33mServer closing\033[0;33m")
try:
    ClientSocket.close()
    ServerSocket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
    ServerSocket.close() # Frees up RAM?
    print("\033[0;32mServer closed\033[0;32m")
except Exception:
    print(Exception)

# Hoggers birthday in 49 days from 26/3