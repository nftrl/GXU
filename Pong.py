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
        self.image = pygame.Surface((9, 75))
        self.image.fill(color_player)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = starting_position

        # movement chars and speed
        (self.up, self.down) = keys  # unpack keys
        self.speed = speed

    def update(self, ks):
        if ks[self.up]:
            self.rect.move_ip(0, -self.speed)
        if ks[self.down]:
            self.rect.move_ip(0, self.speed)

        (_, y) = self.rect.center
        if y < 0:
            self.rect.move_ip(0, self.speed)
        if y > screen_height:
            self.rect.move_ip(0, -self.speed)


# A class that represents balls in the game
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, x_vel, y_vel):
        # this initialises the class.
        # It does a lot of things in the background
        # that we do not have to worry about :)
        super().__init__()

        # the visual block or image that we see
        self.image = pygame.Surface((4, 4))
        self.image.fill(color_ball)

        # used for position
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.x_velocity = x_vel
        self.y_velocity = y_vel

    def update(self):
        self.rect.move_ip(self.x_velocity, self.y_velocity)

        (x, y) = self.rect.center
        if x < 0 or x > screen_width:
            self.x_velocity *= -1
        if y < 0 or y > screen_height:
            self.y_velocity *= -1

    def scale_speed(self, scalar: float):
        self.x_velocity *= scalar
        self.y_velocity *= scalar


# Global variables
fps = 120

screen_width = 600
screen_height = 500

color_background = (10, 180, 60)
color_player = (140, 5, 15)
color_ball = (190, 5, 15)

# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode((screen_width, screen_height))

# Sprites
# sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
balls = pygame.sprite.Group()

# players
player1 = Player((30, screen_height / 2),
                 (pygame.K_w, pygame.K_s), 7)
players.add(player1)
all_sprites.add(player1)

player2 = Player((screen_width - 30, screen_height / 2),
                 (pygame.K_UP, pygame.K_DOWN), 7)
players.add(player2)
all_sprites.add(player2)

for i in range(1):
    ball = Ball(400, 2 * i, 1 + i % 5, 1 + i % 9)
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

    # add ball
    if ks[pygame.K_t]:
        ball = Ball(400, 2 * i, 1 + i % 5, 1 + i % 9)
        balls.add(ball)
        all_sprites.add(ball)

    # ball movespeed
    delta = 0.1
    if ks[pygame.K_r]:
        for ball in balls:
            ball.scale_speed(1 + delta)
    if ks[pygame.K_f]:
        for ball in balls:
            ball.scale_speed(1 - delta)

    # update sprites
    players.update(ks)
    balls.update()

    # collision
    collided = pygame.sprite.groupcollide(players, balls, dokilla=False, dokillb=False)
    for player in collided:
        for ball in collided[player]:
            ball.x_velocity *= -1

    # draw sprites on the screen
    all_sprites.draw(screen)

    # execute the drawing to the screen
    pygame.display.flip()

    # handle fps
    clock.tick(fps)

# Done! Time to quit.
pygame.quit()
