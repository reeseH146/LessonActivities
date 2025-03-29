import socket
import time as t
import threading as th

# Main loop
print("\033[0;33mLoading game\033[0;33m")
# Creates a socket
try: 
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    #ClientSocket.setblocking(False)
    print("Socket successfully created")
except socket.error: 
    print(f"socket creation failed : {socket.error}")
# Connects to server
try:
    Port = 12345 # Default port
    HostIp = "127.0.0.1"
    ClientSocket.connect((HostIp, Port))
    print("Socket successfully connected to Reese LAN Pong server.") 
except socket.gaierror: 
    # this means could not resolve the host 
    print("Could not resolve to host : Reese LAN Pong server.")
    raise SystemExit

# Main game
ClientNumber = "-1"
while True:
    if (t.time() % 1) == 0:
        try:
            ServerData = ClientSocket.recv(1024).decode("utf-8") # Polls for incoming data 
            if "ClientNumber:" in ServerData:
                ClientNumber = ServerData[-1]
            print(ServerData)
            ClientSocket.send(f"Client {ClientNumber} connected".encode("utf-8"))
        except Exception:
            print(f"ERROR : Problem with connection : {Exception}")
            break

# Closes socket and program
print("Client closing")
ClientSocket.shutdown(socket.SHUT_RDWR)
ClientSocket.close()
print("Client closed")