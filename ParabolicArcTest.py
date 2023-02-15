import pygame
import math

screen_width = 1200
screen_height = 500
color_white = (255, 255, 255)
color_black = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius - 1, width=5)

    @staticmethod
    def calcPath(startx, starty, power, ang, time):
        pass


def drawScreen():
    screen.fill((65, 65, 65))
    Ball.draw(screen)
    pygame.draw.line(screen,color_black,line[0],line[1])
    pygame.display.update()



Ball = ball(screen_width / 2, screen_height - 5, 5, color_white)

x = 0
y = 0
power = 0
ang = 0
shoot = False

run = True
while run:
    mouse = pygame.mouse.get_pos()
    #linje mellem ball og mus
    line = [(Ball.x, Ball.y), mouse]
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
                #distance mellem mus og bold
                power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/8
                print("distance is",power*8)
                shoot = False

pygame.quit()
