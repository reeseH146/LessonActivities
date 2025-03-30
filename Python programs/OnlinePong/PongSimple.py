import pygame as pg
import random as r
import socket as soc

# Paddle entity
class PaddleEntity:
    def __init__(self, Position, Colour):
        self.Position = Position
        self.Colour = Colour
        self.Speed = 0.5
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

# Main program
ScreenDimensions = [1920 * 0.6, 1080 * 0.6]
Window = pg.display.set_mode(ScreenDimensions)
Window.fill((96, 176, 90))
pg.display.flip()
Clock = pg.time.Clock()

Player1 = PaddleEntity([int(ScreenDimensions[0] * 0.02), int(ScreenDimensions[1] * 0.5)], (200, 20, 20))
Player2 = PaddleEntity([int(ScreenDimensions[0] * 0.98), int(ScreenDimensions[1] * 0.5)], (20, 20, 200))
Ball = BallEntity([int(ScreenDimensions[0] * 0.5), int(ScreenDimensions[1] * 0.5)], (204, 159, 63), 30)

# Main loop
while True:
    for event in pg.event.get():
        if (event.type == pg.QUIT) or (event.type == pg.K_ESCAPE):
            pg.quit()
            quit()
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
    
    Window.fill((96, 176, 90))
    Player1.Display()
    Player2.Display()
    Ball.Move()
    Ball.Display()
    pg.display.update()
    Clock.tick(60)