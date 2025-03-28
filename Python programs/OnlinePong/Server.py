import socket
import time as t
import threading as th

"""
class Socket:
    def __init__(self, ServerIP, Port):
        Port = 12345 # default port for socket
        # Creates server socket
        try: 
            ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
            print ("\033[0;32mSocket successfully created\033[0;32m")
        except socket.error: 
            print(f"\033[0;31msocket creation failed : {socket.error}\033[0;31m")
        try:
            ServerSocket.bind(("", Port)) # Binds socket to address at port, empty address means server listens for all network
            print(f"\033[0;33mSocket binded at port {Port}\033[0;33m")
            ServerSocket.listen(2) # Listens for incoming connections, backlog is 2 meaning max connections
            print("\033[0;33mListening for incomming connections\033[0;33m")
            return ServerSocket
        except Exception:
            print(f"\033[0;31m{Exception}\033[0;31m")

        Port = 12345 # default port for socket
    
    def Connect(self):
        pass

    def Send(self):
        pass

    def Receive(self):
        pass

    def Close(self):
        print("Client closing")
        self.Socket.shutdown(socket.SHUT_RDWR)
        self.Socket.close()
        print("Client closed")"""

# Main
print("Starting server")

Port = 12345 # default port for socket
# Creates server socket
try: 
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    print ("\033[0;32mSocket successfully created\033[0;32m")
except socket.error: 
    print(f"\033[0;31msocket creation failed : {socket.error}\033[0;31m")
try:
    ServerSocket.bind(("", Port)) # Binds socket to address at port, empty address means server listens for all network
    print(f"\033[0;33mSocket binded at port {Port}\033[0;33m")
    ServerSocket.listen(2) # Listens for incoming connections, backlog is 2 meaning max connections
    print("\033[0;33mListening for incomming connections\033[0;33m")
except Exception:
    print(f"\033[0;31m{Exception}\033[0;31m")

Clients = []
while len(Clients) < 2:
    try:
        # Assigns client onto dictionary of clients
        ClientSocket, Address = ServerSocket.accept()
        Clients.append([ClientSocket, Address])
        #Clients.append([ClientSocket, Address])
        print(f"Got connection from {Address}")
    except Exception:
        print(Exception)

EndTime = t.time() + 600
while t.time() < EndTime:
    if (t.time() % 2) == 0:
        print(t.time())
    else:
        try:
            for Client in Clients:
                Client[0].send("Hello client".encode("utf-8"))
                print(Client[0].recv(2048).decode("utf-8"))
        except Exception:
            print(Exception)

# Closes socket and program
print("Server closing")
try:
    ClientSocket.close()
    ServerSocket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
    ServerSocket.close() # Frees up RAM?
    print("Server closed")
except Exception:
    print(Exception)

# Hoggers birthday in 49 days from 26/3