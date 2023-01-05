"""
This is an unfinished game of pong.
Below are some steps that you can follow to make it behave like regular pong.

TODO
- Add another player
- Set the players starting position to the sides of the screen
- Do so they can only move up and down
- Make the ball 'bounce off' of the edges

Of course you are also welcome to change it in any way you would like :)
"""

import pygame

# A class that represents a player in the game
class Player(pygame.sprite.Sprite):
    def __init__(self, starting_position, keys, speed):
        """
        parameters:
          starting_position   stating position
          keys                a 4-tuple of the keys that are checked
                              in update() for moving up,down,left,right
          speed               the speed of the movement
        """

        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        self.image = pygame.Surface((20,100))
        self.image.fill(color_player)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = starting_position

        # movement chars and speed
        (self.up, self.down, self.left, self.right) = keys # unpack keys
        self.speed = speed

    def update(self, ks):
        if ks[self.up]:
            self.rect.move_ip(0, -self.speed)
        if ks[self.down]:
            self.rect.move_ip(0, self.speed)
        if ks[self.left]:
            self.rect.move_ip(-self.speed, 0)
        if ks[self.right]:
            self.rect.move_ip(self.speed, 0)

# A class that represents balls in the game
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        # NOTE: no parameters
 
        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        self.image = pygame.Surface((10,10))
        self.image.fill(color_ball)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = (20,20)

    def update(self):
        # NOTE: no parameters
 
        self.rect.move_ip(1,1)

# Global variables
fps = 60

screen_width = 800
screen_height = 800

color_background = (10,180,60)
color_player = (140,5,15)
color_ball = (140,60,26)

# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Sprites
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
balls = pygame.sprite.Group()

player1 = Player((screen_width/2, screen_height/2), (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d), 7)
players.add(player1)
all_sprites.add(player1)

ball = Ball()
balls.add(ball)
all_sprites.add(ball)

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

    # update sprites
    players.update(ks)
    balls.update()

    # draw sprites on the screen
    all_sprites.draw(screen)
    
    # execute the drawing to the screen
    pygame.display.flip()

    # handle fps
    clock.tick(fps)


# Done! Time to quit.
pygame.quit()
