import pygame
import math

# TODO
# Create player
# Create all from pos of player
# Turns
# Powerups/Store?


# Credit to tech with tim @yt
screen_width = 1200
screen_height = 500
color_white = (255, 255, 255)
color_black = (255, 255, 255)
color_green = (25, 255, 25)
screen = pygame.display.set_mode((screen_width, screen_height))


class player(pygame.sprite.Sprite):
    def __init__(self, x, y, keys, speed):

        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        self.image = pygame.Surface((25, 10))
        self.image.fill(color_green)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        (self.A, self.D) = keys  # unpack keys
        self.speed = speed

    def update(self, ks):
        if ks[self.A]:
            self.rect.move_ip(-self.speed, 0)
        if ks[self.D]:
            self.rect.move_ip(self.speed, 0)
        (x, _) = self.rect.center
        if x < 0 + 10:
            self.rect.move_ip(self.speed, 0)
        if x > screen_width - 10:
            self.rect.move_ip(-self.speed, 0)


class ball(object):
    def __init__(self, x, y, x_vel, y_vel, radius, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius - 1, width=5)

  #  @staticmethod
 #   def boundaryCheck(startx, starty):


    @staticmethod
    def calcPath(startx, starty, power, ang, time):
        x_vel = math.cos(ang) * power
        y_vel = math.sin(ang) * power
        # X distance meget nem da det er hastighed gange tid
        distX = x_vel * time
        # Motion with downwards acceleration
        distY = (y_vel * time) + ((-4.9 * time ** 2) / 2)
        newX = round(distX + startx)
        if newX < 0:
            newX = 0+Ball.radius
        elif newX > screen_width:
            newX = screen_width-Ball.radius

        newY = round(starty - distY)

        return newX, newY


def drawScreen():
    screen.fill((65, 65, 65))
    Ball.draw(screen)
    players.draw(screen)
    pygame.draw.line(screen, color_black, line[0], line[1])
    pygame.display.update()


def getAngle(mouse):
    sX = Ball.x
    sY = Ball.y
    try:
        angle = math.atan((sY - mouse[1]) / (sX - mouse[0]))
    except:
        angle = math.pi / 2
    # Tjekker hvilken kvadrant på enhedscirklen.
    if mouse[1] < sY and mouse[0] > sX:
        angle = abs(angle)
    elif mouse[1] < sY and mouse[0] < sX:
        angle = math.pi - angle
    elif mouse[1] > sY and mouse[0] < sX:
        angle = math.pi + abs(angle)
    elif mouse[1] > sY and mouse[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


# variables
players = pygame.sprite.Group()
balls = pygame.sprite.Group()

Ball = ball(screen_width / 2, screen_height - 5, 0, 0, 5, color_white)
# balls.add(Ball)
Player1 = player(screen_width / 3, screen_height - 5, (pygame.K_a, pygame.K_d), 1)
players.add(Player1)
x = 0
y = 0
power = 0
ang = 0
shoot = False

run = True
while run:
    # get key presses
    ks = pygame.key.get_pressed()
    if shoot:
        if (Ball.y < screen_height - Ball.radius):
            time += 0.025
            # print(ang)
            po = ball.calcPath(x, y, power, ang, time)
            Ball.x = po[0]
            Ball.y = po[1]
        else:
            shoot = False
            Ball.y = screen_height - 6

    mouse = pygame.mouse.get_pos()
    # linje mellem ball og mus
    line = [(Ball.x, Ball.y), mouse]
    players.update(ks)
    drawScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = Ball.x
                y = Ball.y
                time = 0
                # distance mellem mus og bold
                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 8
                # print("distance is", power * 8)
                ang = getAngle(mouse)
                print(ang)
    # collision
#    collided = pygame.sprite.spritecollide(players, balls, dokilla=True, dokillb=False)
#    for player in collided:
#        for ball in collided[player]:
#            ball.x_velocity *= -1


pygame.quit()
