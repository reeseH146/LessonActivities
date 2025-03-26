import socket
import time as t

# Creates a socket
try: 
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    print ("Socket successfully created")
except socket.error: 
    print(f"socket creation failed : {socket.error}")

Port = 80 # default port for socket

"""
try:
    # Pings host
    HostName = "www.google.com"
    host_ip = socket.gethostbyname(HostName)
    # Connects to host/serverr 
    Socket.connect((host_ip, port))
    print(f"Socket successfully connected to {HostName}") 
except socket.gaierror: 
# this means could not resolve the host 
    print (f"Could not resolve to host : {HostName}")
    raise SystemExit
"""

Socket.bind(("", Port)) # Binds socket to address with port, address is empty means it will try to listen for incomming connections on the network
print(f"Socket binded at port {Port}")
MaxDeclined = 2
Socket.listen(MaxDeclined) # Listens for incoming connections, 2 is the backlog which standsfor the amount of unaccepted 
print(f"Listening for incomming connections : Max number of unaccepted {MaxDeclined}")

Hours = 0.1
TargetTime = t.time() + 60#(3600 * Hours)
StartTime = t.time()
while t.time() < TargetTime:
    c, Address = Socket.accept()     
    print(f"Got connection from {Address}")
    if (t.time() - StartTime) % 2 == 0:
        c.send("Thank you for connecting".encode())
    print("Sent message 1")

# Closes socket and program
print("Server closing")
Socket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
Socket.close() # Frees up RAM?
print("Server closed")

# Hoggers birthday in 49 days from 26/3