import pygame
import math
import random

# Global variables
fps = 60
screen_width = 800
screen_height = 800
color_background = (10,180,60)

class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position, up, down, left, right):
        super().__init__()

        self.image = pygame.Surface((screen_width/20,screen_height/20))
        self.image.fill((200,30,0))

        self.rect = self.image.get_rect()
        self.rect.center= starting_position

        self.speed = 3

        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def update(self, ks):
        if ks[self.up]:
            self.rect.move_ip(0,-self.speed)
        if ks[self.left]:
            self.rect.move_ip(-self.speed,0)
        if ks[self.down]:
            self.rect.move_ip(0,self.speed)
        if ks[self.right]:
            self.rect.move_ip(self.speed,0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, starting_position, speed_x, speed_y):
        super().__init__()

        self.image = pygame.Surface((screen_width/20,screen_height/20))
        self.image.fill((200,30,0))

        self.rect = self.image.get_rect()
        self.rect.center= starting_position

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, ks):
        self.rect.move_ip((self.speed_x, self.speed_y))

# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Sprites
player1 = Player((screen_width/2, screen_height/2),
                 pygame.K_w, pygame.K_s,
                 pygame.K_a, pygame.K_d)
player2 = Player((20, screen_height/2),
                 pygame.K_UP, pygame.K_DOWN,
                 pygame.K_LEFT, pygame.K_RIGHT)

enemy1 = Enemy((screen_width/2, screen_height/2), 1,-3)

player_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player_sprites.add(player1)
all_sprites.add(player1)
player_sprites.add(player2)
all_sprites.add(player2)
enemy_sprites.add(enemy1)
all_sprites.add(enemy1)

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
