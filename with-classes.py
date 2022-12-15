import pygame
import math
import random

# Global variables
fps = 60

screen_width = 800
screen_height = 800

color_background = (10,180,60)

class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        super().__init__()

        self.image = pygame.Surface((screen_width/20,screen_height/20))
        self.image.fill((200,30,0))

        self.rect = self.image.get_rect()
        self.rect.center= starting_position

        self.speed = 3

    def update(self, ks):
        if ks[pygame.K_w]:
            self.rect.move_ip(0,-self.speed)
        if ks[pygame.K_a]:
            self.rect.move_ip(-self.speed,0)
        if ks[pygame.K_s]:
            self.rect.move_ip(0,self.speed)
        if ks[pygame.K_d]:
            self.rect.move_ip(self.speed,0)


# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Sprites
player1 = Player((screen_width/2, screen_height/2))

all_sprites = pygame.sprite.Group()
all_sprites.add(player1)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Fill the background
    screen.fill(color_background)

    # get key presses
    ks = pygame.key.get_pressed()

    all_sprites.update(ks)
    all_sprites.draw(screen)

    
    # Flip the display (execute the drawing to the screen)
    pygame.display.flip()
    clock.tick(fps)

# Done! Time to quit.
pygame.quit()
