import socket
import time as t

"""
Originally more complicated, server would dynamically connect and manage clients
Now 2 clients only are required for LAN game, they must be connected which means server and client code doesn't need to be designed to bend their backs to keep clients connected and communicating at the same time
"""

# Main
print("\033[0;33mStarting server\033[0;33m")

# Creates server socket
try: 
    # Socket creation
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    # Prepares socket for connections
    Port = 12345 # default port for socket
    ServerSocket.bind(("", Port)) # Binds socket to address at port, empty address means server listens for all network
    print(f"\033[0;33mSocket binded at port {Port}\033[0;33m")
    ServerSocket.listen(2) # Listens for incoming connections, backlog is 2 meaning max connections
    print("\033[0;32mSocket successfully created\033[0;32m")
    print("\033[0;33mListening for incomming connections\033[0;33m")
except socket.error: 
    print(f"\033[0;31mERROR : socket creation failed : {socket.error}\033[0;31m")
    raise SystemExit

# Connects 2 clients together
Clients = []
ClientCount = 0
while len(Clients) < 2:
    try:
        # Accepts clients and records them
        ClientSocket, Address = ServerSocket.accept()
        Clients.append([ClientSocket, Address])
        print(f"\033[0;32mGot connection from {Address}\033[0;32m")
        # Checks client is connected
    except Exception:
        print(f"\033[0;31mERROR : Cannot accept to client{Exception}\033[0;31m")

# Checks clients have connected and server is ready to interact with clients
for Client in Clients:
    try:
        Client[0].send(f"Acknowledged C{Clients.index(Client) + 1}".encode("utf-8"))
        """        ClientData = Client.recv(128).decode("utf-8")
        if ClientData == "Client ready":
            continue"""
    except:
        # Closes socket and program
        print("Client unable to respond.")
        print("\033[0;33mServer closing\033[0;33m")
        ServerSocket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
        ServerSocket.close() # Frees up RAM?
        print("\033[0;32mServer closed\033[0;32m")
        SystemExit

# While both clients connected, continues to sync game data
PreviousTime = t.time()
while True:
    # Every second, polls to check clients are connected and syncs game data
    CurrentTime = t.time()
    if (CurrentTime - PreviousTime) > (1):
        PreviousTime = CurrentTime
        try:
            # Goes through both clients
            for Client in Clients:
                # Checks client is connected
                print(1)
                try:
                    Client[0].send(f"\033[0;34mHello client {Clients.index(Client) + 1}\033[0;34m".encode("utf-8"))
                    print(2)
                    ClientData = Client[0].recv(128).decode("utf-8") # ASCII characters in utf-8 is 1 byte
                except socket.timeout:
                    print("Client timed out")
                except BlockingIOError:
                    print(BlockingIOError)
                    pass
                else:
                    print(3)
                    if not ClientData:# (ClientData == b"") or (ClientData == ""):
                        break
                    # Syncs data with that client
                    else:
                        print(ClientData)
        # If either clients disconnects then closes the game
        except Exception:
            print(f"\033[0;31mERROR : {Exception}\033[0;31m")
            break

# Closes socket and program
print("\033[0;33mServer closing\033[0;33m")
try:
    ServerSocket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
    ServerSocket.close() # Frees up RAM?
    print("\033[0;32mServer closed\033[0;32m")
except Exception:
    print(Exception)