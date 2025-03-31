import socket
import time as t

"""
Originally more complicated, server would dynamically connect and manage clients
Now 2 clients only are required for LAN game, they must be connected which means server and client code doesn't need to be designed to bend their backs to keep clients connected and communicating at the same time

Now cause
"""

# Main
print("\033[0;33mStarting server\033[0;33m")

# Creates server socket
try: 
    # Socket creation
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    # Prepares socket for connections
    Port = 12345 # default port for socket
    ServerIP = socket.gethostbyname(socket.gethostname())
    print(ServerIP)
    ServerSocket.bind((ServerIP, Port)) # Binds socket to address at port, empty address means server listens for all network
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
        Client[0].settimeout(10)
    except:
        # Closes socket and program
        print("Client unable to respond.")
        print("\033[0;33mServer closing\033[0;33m")
        ServerSocket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
        ServerSocket.close() # Frees up RAM?
        print("\033[0;32mServer closed\033[0;32m")
        SystemExit

ClientPositions = []
PreviousTime = t.time()
while True:
    # Every second, polls to check clients are connected and syncs game data
    CurrentTime = t.time()
    if (CurrentTime - PreviousTime) > (1):
        PreviousTime = CurrentTime
        try:
            print(2)
            # Checks client is connected
            ClientPositions[0] = Clients[0][0].recv(128).decode("utf-8") # ASCII characters in utf-8 is 1 byte
            print(ClientPositions)
            if ClientPositions[0]:
                Clients[1][0].sendall("Ready".decode("uft-8"))
                ClientPositions[1] = Clients[1][0].recv(128).decode("utf-8") # ASCII characters in utf-8 is 1 byte
            else:
                print("Help")
            print(ClientPositions)
            print(3)
            if not ClientPositions[0]:
                print(4)
                continue
            else:
                print(5)
                Clients[0][0].sendall(f"{ClientPositions[1]}".encode("utf-8"))
            if not ClientPositions[1]:
                print(6)
                break
            else:
                print(7)
                Clients[1][0].sendall(f"{ClientPositions[0]}".encode("utf-8"))
            ClientPositions = []
        # If either clients disconnects then closes the game
        except Exception:
            print(f"\033[0;31mERROR : {Exception}\033[0;31m")

# Closes socket and program
print("\033[0;33mServer closing\033[0;33m")
try:
    ServerSocket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
    ServerSocket.close() # Frees up RAM?
    print("\033[0;32mServer closed\033[0;32m")
except Exception:
    print(Exception)


"""
Who is going to MC movie
Reese
Josh
Ralfs
Zeke
"""