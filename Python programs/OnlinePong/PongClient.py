import socket
import time as t

# Creates a socket
try: 
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket which only accefts IPv4 AddressFamily (AF), and TCP type connection
    print ("Socket successfully created")
except socket.error: 
    print(f"socket creation failed : {socket.error}")

Port = 80 # default port for socket


try:
    # Pings host
    HostName = "www.google.com"
    HostIp = "10.18.71.46"
    # Connects to host/serverr 
    Socket.connect((HostIp, Port))
    print(f"Socket successfully connected to {HostName}") 
except socket.gaierror: 
# this means could not resolve the host 
    print (f"Could not resolve to host : {HostName}")
    raise SystemExit

Hours = 0.5
TargetTime = t.time() + (3600 * Hours)
while t.time() < TargetTime:
    if (t.time() % 3 == 0) and (t.time() % 7 == 0):
        print(1)
    print(Socket.recv(1024).decode())
"""TargetTime = t.time() + (3600 * Hours)
while t.time() < TargetTime:
    c, Address = Socket.accept()     
    print(f"Got connection from {Address}")
    
    c.send("Thank you for connecting".encode()) """

# Closes socket and program
print("Client closing")
Socket.shutdown(socket.SHUT_RDWR) # Force closes all RW processes?
Socket.close() # Frees up RAM?
print("Client closed")

# Hoggers birthday in 49 days from 26/3
