import pygame
import math
import random

# Global variables
fps = 60
screen_width = 800
screen_height = 800
color_background = (10,180,60)

# Class for players of the game
class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position, up, down, left, right):
        super().__init__()

        # Create player figure
        self.image = pygame.Surface((20,20))
        self.image.fill((200,30,0))

        # Get rect of player. Wi will use this for movement and collision detection
        self.rect = self.image.get_rect()
        self.rect.center= starting_position

        # Set movement speed, used in 'update'
        self.speed = 3

        # Set movement keys
        # note 'up' 'down' 'left' 'right' are an input to
        # '__init__' function
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    # Function used to update instance
    # we will run this every frame of the game
    def update(self, ks):
        # Move on the given movement keys
        if ks[self.up]:
            self.rect.move_ip(0,-self.speed)
        if ks[self.left]:
            self.rect.move_ip(-self.speed,0)
        if ks[self.down]:
            self.rect.move_ip(0,self.speed)
        if ks[self.right]:
            self.rect.move_ip(self.speed,0)

# Class for enemies in the game
# Doesn't really do much now
class Enemy(pygame.sprite.Sprite):
    def __init__(self, starting_position, speed_x, speed_y):
        super().__init__()

        # enemy figure
        self.image = pygame.Surface((20,20))
        self.image.fill((200,30,0))

        self.rect = self.image.get_rect()
        self.rect.center= starting_position

        # movement speed. this class moves with a fixed speed because of the current implementation of 'update'
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, ks):
        # move with fixed speed
        self.rect.move_ip((self.speed_x, self.speed_y))

# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Sprites
# - player1 moves on wasd
# - player2 moves on arrow keys
# - enemy1 is set to fixed movementspeed on (1,-3)
player1 = Player((screen_width/2, screen_height/2),
                 pygame.K_w,
                 pygame.K_s,
                 pygame.K_a,
                 pygame.K_d)

player2 = Player((20, screen_height/2),
                 pygame.K_UP,
                 pygame.K_DOWN,
                 pygame.K_LEFT,
                 pygame.K_RIGHT)

enemy1 = Enemy((screen_width/2, screen_height/2), 1, -3)

# Create sprite groups
player_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Add sprites to groups
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

    # Update all the sprites in 'all_sprites'
    all_sprites.update(ks)

    # Draw all the sprites in 'all_sprites'
    all_sprites.draw(screen)
    
    # Flip the display (execute the drawing to the screen)
    pygame.display.flip()

    # Manage FPS
    clock.tick(fps)


# Done! Time to quit.
pygame.quit()
