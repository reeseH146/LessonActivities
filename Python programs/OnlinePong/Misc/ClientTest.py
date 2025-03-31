import socket
import time as t
import pygame as pg

# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #

# Loading networking aspect of game
print("\033[0;33mLoading game\033[0;33m")
# Creates a socket
try: 
    # Socket creation
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    print("\033[0;32mSocket successfully created\033[0;32m")
except socket.error: 
    print(f"\033[0;31mERROR : socket creation failed : {socket.error}\033[0;31m")
    raise SystemExit
else:
    try:
        Port = 12345 # Default port
        HostIp = "127.0.0.1" # LAN IP
        ClientSocket.connect((HostIp, Port))
        print("\033[0;32mSocket successfully connected to Reese LAN Pong server.\033[0;32m") 
    except Exception:
        print(f"\033[0;31mERROR : Host not connectable : {socket.error}\033[0;31m")
        raise SystemExit

# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #

# Main game
GameOn = False
ClientNumber = -1
# Waits to be acknowledged by the server to start
while True:
    try:
        ServerData = ClientSocket.recv(128).decode("utf-8")
        if ServerData:
            ClientNumber = ServerData[-1]
            GameOn = True
            print(ClientNumber)
            break
    except:
        print("Waiting on server")

PreviousTime = t.time()
# Games run until connection breaks or someone loses
# Main loop
while GameOn:
    # Exchanges data with the server every second
    CurrentTime = t.time()
    if (CurrentTime - PreviousTime) > (1):
        PreviousTime = CurrentTime
        try:
            try:
                ClientSocket.send(f"Client {ClientNumber} connected".encode("utf-8"))
                ServerData = ClientSocket.recv(512).decode("utf-8") # Polls for incoming data 
                print(ServerData)
            except socket.timeout:
                print("Server timed out")
        except Exception:
            print(f"ERROR : Problem with connection : {Exception}")
            break


# Closes socket and program
print("\033[0;33mServer closing\033[0;33m")
ClientSocket.shutdown(socket.SHUT_RDWR)
ClientSocket.close()
print("\033[0;32mServer closed\033[0;32m")