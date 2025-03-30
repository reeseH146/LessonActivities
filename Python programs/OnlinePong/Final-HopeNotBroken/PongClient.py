import socket
import time as t
import pygame as pg

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
        self.Speed = 10
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
        self.SpeedX = 7
        Temp = 7
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
# Loads game assets
ScreenDimensions = [1920 * 0.6, 1080 * 0.6]
Window = pg.display.set_mode(ScreenDimensions)
Window.fill((96, 176, 90))
pg.display.flip()
Clock = pg.time.Clock()

Player1 = PaddleEntity([int(ScreenDimensions[0] * 0.02), int(ScreenDimensions[1] * 0.5)], (200, 20, 20))
Player2 = PaddleEntity([int(ScreenDimensions[0] * 0.98), int(ScreenDimensions[1] * 0.5)], (20, 20, 200))
Ball = BallEntity([int(ScreenDimensions[0] * 0.5), int(ScreenDimensions[1] * 0.5)], (204, 159, 63), 30)

# Waits to be acknowledged by the server to start
GameOn = False
ClientNumber = -1
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
            if ClientNumber == 1:
                ClientSocket.send(f"{Player1.Position[1]}".encode("utf-8"))
            else:
                ClientSocket.send(f"{Player2.Position[1]}".encode("utf-8"))
            ServerData = ClientSocket.recv(512).decode("utf-8") # Polls for incoming data 
            if ClientNumber == 1:
                Player2.Position[1] = int(ServerData)
            else:
                Player1.Position[1] = int(ServerData)

        except Exception:
            print(f"ERROR : Problem with connection : {Exception}")
            break
    # Interacts with game
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (event.type == pg.K_ESCAPE):
            pg.quit()
            break
    KeysPressed = pg.key.get_pressed()
    if KeysPressed[pg.K_ESCAPE]:
        pg.quit()
        quit()
    if KeysPressed[pg.K_w]:
        Player1.Move(0)
    elif KeysPressed[pg.K_s]:
        Player1.Move(1)
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
    Clock.tick(60)

# Closes socket and program
print("\033[0;33mServer closing\033[0;33m")
ClientSocket.shutdown(socket.SHUT_RDWR)
ClientSocket.close()
print("\033[0;32mServer closed\033[0;32m")