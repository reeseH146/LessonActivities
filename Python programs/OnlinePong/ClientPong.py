import socket
import time as t
import pygame as pg
import select

# Code not updating on PC from laptop so forcing merge conflict

# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #

# Paddle entity
class PaddleEntity:
    def __init__(self, Position, Colour):
        self.Position = Position
        self.Colour = Colour
        self.Speed = 13
        self.Dimensions = [20, 1080 * 0.6 * 0.3]
        self.rect = pg.Rect(int(self.Position[0]), int(self.Position[1]), self.Dimensions[0], self.Dimensions[1])
    
    # Just reassigns rect position as position and blits
    def Display(self):
        # Reassigns rect position and then blits onto screen
        self.rect.center = (int(self.Position[0]), int(self.Position[1]))
        pg.draw.rect(Window, self.Colour, self.rect)

    """
    Uses 1/0 rather than ws or UPDOWN to allow for flexible mapping of keybinds for each entity
    1 for up, 0 for down since it increments/decrements but could be misinterpreted as 0 for approaching 0 and 1 for increasing from 0

    Recalculates position to prevent ball from going off the map : 
     - (self.Position[1] + (self.Dimensions[1] * 0.5)) > ScreenDimensions[1]:
       Means if bottom of paddle (centre pos + half length) if further than bottom of screen
     - self.Position[1] = ScreenDimensions[1] - (self.Dimensions[1] * 0.5)
       Means reset centre position so bottom of paddle touches bottom of screen by removing bottom of screen with half of paddle
    This repeats for going through the top but inverse
    """
    def Move(self, Direction):
        # Moves paddle
        if Direction == 1: # Moves up approaching 0
            self.Position[1] += self.Speed
        elif Direction == 0: # Moves down approaching y-length of display
            self.Position[1] -= self.Speed
        # Prevents paddle moving off the screen
        if (self.Position[1] + (self.Dimensions[1] * 0.5)) > ScreenDimensions[1]: # Prevents going through the bottom
            self.Position[1] = ScreenDimensions[1] - (self.Dimensions[1] * 0.5)
        elif self.Position[1] - (self.Dimensions[1] * 0.5)< 0:  # Prevents going through the top
            self.Position[1] = self.Dimensions[1] * 0.5

# Ball entity
class BallEntity:
    def __init__(self, Position, Colour, Radius):
        self.Position = Position
        self.Radius = Radius
        self.Colour = Colour
        self.SpeedX = 0
        Temp = 1
        self.SpeedY = Temp
        self.Dimensions = [20, 1080 * 0.6 * 0.3]
        self.HitBox = pg.Rect(int(self.Position[0]), int(self.Position[1]), self.Radius * 2, self.Radius * 2)
        self.HitBox.center = self.Position

    # Literally blits
    def Display(self):
        pg.draw.circle(Window, self.Colour, self.Position, self.Radius)

    """
    Moves ball position
    Checks for interaction with border
     - If touches top or bottom of the screen
     - Flips speed

    """
    def Move(self):
        # Moves ball position
        self.Position[0] += self.SpeedX
        self.Position[1] += self.SpeedY
        self.HitBox.center = self.Position
        # Prevents ball from moving out of the border
        if ((self.Position[1] - self.Radius) < 0) or (self.Position[1] + self.Radius) > ScreenDimensions[1]:
            self.SpeedY *= -1
        # Ends game
        if ((self.Position[0] - self.Radius) < 0) or ((self.Position[0] + self.Radius) > ScreenDimensions[0]):
            pg.time.wait(1000)
            quit()
        if self.HitBox.colliderect(Player1.rect):
            self.SpeedX *= -1
            self.Position[0] = Player1.Position[0] + (Player1.Dimensions[0] * 0.5) + self.Radius
            self.HitBox[0] = Player1.Position[0] + (Player1.Dimensions[0] * 0.5) + self.Radius
        elif (self.HitBox.colliderect(Player2.rect)):
            self.SpeedX *= -1
            self.Position[0] = Player2.Position[0] - (Player2.Dimensions[0] * 0.5) - self.Radius
            self.HitBox[0] = Player2.Position[0] - (Player2.Dimensions[0] * 0.5) - self.Radius

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

# Connects to host
while True:
    try:
        Port = 12345 # Default port
        HostIp = socket.gethostbyname(socket.gethostname())#"10.18.71.23" # LAN IP
        ClientSocket.connect((HostIp, Port))
        print("\033[0;32mSocket successfully connected to Reese LAN Pong server.\033[0;32m") 
        break
    except Exception:
        print(f"\033[0;31mERROR : Host not connectable : {socket.error}\033[0;31m")
        raise SystemExit

# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #
# ----- +++++ ----- +++++ ----- +++++ ----- #

# Main game
# Loads game assets
ScreenDimensions = [1920 * 0.6, 1080 * 0.6]
pg.display.set_caption("Client - Player 2 Pong")
Window = pg.display.set_mode(ScreenDimensions)
Window.fill((96, 176, 90))
pg.display.flip()
Clock = pg.time.Clock()

Player1 = PaddleEntity([int(ScreenDimensions[0] * 0.02), int(ScreenDimensions[1] * 0.5)], (200, 20, 20))
Player2 = PaddleEntity([int(ScreenDimensions[0] * 0.98), int(ScreenDimensions[1] * 0.5)], (20, 20, 200))
Ball = BallEntity([int(ScreenDimensions[0] * 0.5), int(ScreenDimensions[1] * 0.5)], (204, 159, 63), 30)

# Waits to be acknowledged by the server to start
GameOn = False

while True:
    try:
        # Wait for server acknowledgment
        ServerData = ClientSocket.recv(128).decode("utf-8")
        if ServerData == "Acknowledged For Reese LAN Pong Game!":
            print("Server acknowledged, sending ready confirmation...")
            # Send ready confirmation to server
            ClientSocket.sendall("Client For Reese LAN Pong Game Ready!".encode("utf-8"))
            # Get start time from server
            StartTime = float(ClientSocket.recv(128).decode("utf-8"))
            GameOn = True
            print("Game is starting soon!")
            break
    except Exception as e:
        print(f"Waiting on server: {e}")

ClientSocket.setblocking(False)
while t.time() < StartTime:
    pass

# Main game
PreviousTime = t.time()
ClientSocket.settimeout(0.2)
# Games run until connection breaks or someone loses
# Main loop
while GameOn:
    Clock.tick(120)
    ClientSocket.sendall(str(Player2.Position[1]).encode("utf-8"))
    ready_to_read, _, _ = select.select([ClientSocket], [], [], 0)
    if ready_to_read:
        try:
            ServerData = int(ClientSocket.recv(128).decode("utf-8").split(".")[0])
            BallPos = ClientSocket.recv(128).decode("utf-8").split("-")
            if BallPos[0] and BallPos[1] and BallPos[2] and BallPos[3]:
                Ball.Position[0] = int(BallPos[0])
                Ball.Position[1] = int(BallPos[1])
                Ball.SpeedX = int(BallPos[2])
                Ball.SpeedY = int(BallPos[3])
            else:
                print(BallPos)
            if 0 < ServerData < 1080:
                Player1.Position[1] = ServerData
            else:
                print(ServerData)
        except Exception:
            print(Exception)
    
    # Interacts with game
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (event.type == pg.K_ESCAPE):
            pg.quit()
            break
    KeysPressed = pg.key.get_pressed()
    if KeysPressed[pg.K_ESCAPE]:
        pg.quit()
        quit()
    if KeysPressed[pg.K_UP]:
        Player2.Move(0)
    elif KeysPressed[pg.K_DOWN]:
        Player2.Move(1)

    
    # Rests scene
    Window.fill((96, 176, 90))
    Player1.Display()
    Player2.Display()
    Ball.Move()
    Ball.Display()
    pg.display.update()

# Closes socket and program
print("\033[0;33mServer closing\033[0;33m")
ClientSocket.shutdown(socket.SHUT_RDWR)
ClientSocket.close()
print("\033[0;32mServer closed\033[0;32m")