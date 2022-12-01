"""
keys:
    q/a		change number of layers
    w/s		change number of circles per layer
    e/d		change circle radius
    r/f		change jitter amount
    t/g		change fps
    y		set/unset use of clock (fps)
"""
import pygame
import math
import random

def polar_to_cartesian(r,θ):
    """ translate polar (r,θ) coordinates into cartesian (x,y) coordinates
            r	radius
            θ	angle
    """
    x = r * math.cos(θ)
    y = r * math.sin(θ)
    return (x,y)

# Variables used in the code
layers = 13
circles_per_layer = 17 
circle_radius = 5
amount_jitter = 0.01
fps = 30
fps_max = 120
use_clock = True

# colors
color_circle = (10,230,65)
color_background = (255, 0, 0)

# Initialising pygame instance
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen_width = 800
screen_height = 800
dimensions = (screen_width, screen_height)
screen = pygame.display.set_mode(dimensions)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # get key presses
    ks = pygame.key.get_pressed()

    # layers 
    if ks[pygame.K_q]:
        layers += 1
    if ks[pygame.K_a]:
        layers -= 1

    # circles_per_layer 
    if ks[pygame.K_w]:
        circles_per_layer += 1
    if ks[pygame.K_s]:
        circles_per_layer -= 1

    # circle_radius 
    if ks[pygame.K_e]:
        circle_radius += 1
    if ks[pygame.K_d]:
        circle_radius -= 1

    # amount_jitter 
    if ks[pygame.K_r]:
        amount_jitter += 0.001
    if ks[pygame.K_f]:
        amount_jitter -= 0.001

    # fps
    if ks[pygame.K_t]:
        fps += 1
    if ks[pygame.K_g]:
        fps -= 1

    # set / unset use of fps
    if ks[pygame.K_y]:
        use_clock = not use_clock

    # variable boundaries
    if layers < 0:
        layers = 0

    if amount_jitter < 0:
        amount_jitter = 0

    if circles_per_layer < 0:
        circles_per_layer = 0

    if fps < 0:
        fps = 0
    elif fps > fps_max:
        fps = fps_max

    # Fill in the background
    screen.fill(color_background)

    # Draw
    #   i is current layer
    #   j is current circle
    # Polar coordiantes (r,θ) are used to calculate circle position,
    # then translated into cartesian coordinates (x,y) for drawing.
    for i in range(layers):
        layer_radius = min(screen_width,screen_height)/(layers + 1) * (i + 1)
        for j in range(circles_per_layer):
            # Calculate evenly spaced angles, then add a bit of randomness
            θ = 2*math.pi * j / circles_per_layer
            θ += amount_jitter * math.sin(random.uniform(0,2*math.pi))
            # Translate into cartesian (x,y) coordinates
            (x_rel,y_rel) = polar_to_cartesian(layer_radius,θ)
            pos = (x_rel + screen_width/2, y_rel + screen_height/2)
            # Draw the circle
            pygame.draw.circle(screen, color_circle, pos, circle_radius)
    
    # Flip the display (execute the drawings to the screen)
    pygame.display.flip()

    # manage fps (only if use_clock is True)
    if use_clock:
        clock.tick(fps)

# Done! Time to quit.
pygame.quit()
