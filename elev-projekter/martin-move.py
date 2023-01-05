import pygame
from random import random
pygame.init()
# Set up the drawing window
screenx=1360
screeny=700
screen = pygame.display.set_mode([screenx, screeny])
x=screenx / 2
y=screeny / 2
x1=1
y1=1
color1= 255
color2= 255
color3= 255
border= False

speed=1
clock= pygame.time.Clock()
fps= 120
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ks = pygame.key.get_pressed()
    if ks[pygame.K_k]:
        print (f"x:{x}")
        print (f"y:{y}")
        print(f"x1:{x1}")
        print(f"y1:{y1}")
        print (f"speed:{speed}")
        print (f"fps:{fps}")
    if ks[pygame.K_r]:
        fps = fps +1
    if ks[pygame.K_f]:
        fps = fps -1
    if ks[pygame.K_q]:
        speed = speed +0.05
    if ks[pygame.K_e]:
        speed = speed -0.01
    if ks[pygame.K_w]:
        y =y -speed
    if ks[pygame.K_s]:
        y= y +speed
    if ks[pygame.K_d]:
        x= x +speed
    if ks[pygame.K_a]:
        x= x -speed
    if (border==False):
        if (x > screenx):
            x = x - screenx
        if (x < 0):
            x = x + screenx
        if (y > screeny):
            y = y - screeny
        if (y < 0):
            y = y + screeny
    if (border==True):
        if (x > screenx):
            x = x - 10
        if (x < 0):
            x = x + 10
        if (y > screeny):
            y = y - 10
        if (y < 0):
            y = y + 10
    if (border==False):
        if (x1 > screenx):
            x1 = x1 - screenx
        if (x1 < 0):
            x1 = x1 + screenx
        if (y1 > screeny):
            y1 = y1 - screeny
        if (y1 < 0):
            y1 = y1 + screeny
    if (border==True):
        if (x1 > screenx):
            x1 = x1 - 10
        if (x1 < 0):
            x1 = x1 + 10
        if (y1 > screeny):
            y1 = y1 - 10
        if (y1 < 0):
            y1 = y1 + 10
    if ks[pygame.K_t]:
        x = screenx / 2
        y = screeny / 2
    if ks[pygame.K_UP]:
        y1 =y1 -speed
    if ks[pygame.K_DOWN]:
        y1= y1 +speed
    if ks[pygame.K_RIGHT]:
        x1= x1 +speed
    if ks[pygame.K_LEFT]:
        x1= x1 -speed
    if ks[pygame.K_1]:
        color1= 255
        color2= 0
        color3= 0
    if ks[pygame.K_2]:
        color2 = 200
        color1 = 0
        color3 = 0
    if ks[pygame.K_3]:
        color3 = 255
        color2= 0
        color1= 0
    if ks[pygame.K_4]:
        color3= 200
        color2= 0
        color1= 200
    if ks[pygame.K_5]:
        color1=255
        color2=255
        color3=0
    if ks[pygame.K_6]:
        color1=255
        color2=255
        color3=255
    if ks[pygame.K_b]:
         border=True
    if ks[pygame.K_n]:
         border=False
    screen.fill((color1, color2, color3))
    pygame.draw.circle(screen, (0, 255, 255), (x1, y1), 10)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)
    pygame.display.flip()

    clock.tick(fps)
