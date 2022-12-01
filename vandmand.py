"""
keys:
    q/a		change layers
    w/s		change circles per layer
    e/d		change circle radius
    r/f		change jitter
    t/g		change fps
    y		set/unset use of clock
"""
import pygame
import math
import random

def polar_to_cartesian(r,θ):
    x = r * math.cos(θ)
    y = r * math.sin(θ)
    return (x,y)

# Variables used in the code
layers = 13
circles_per_layer = 17 
circle_radius = 5
rnd_scalar = 0.01
fps = 30
fps_max = 120
use_clock = True

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

    # rnd_scalar 
    if ks[pygame.K_r]:
        rnd_scalar += 0.001
    if ks[pygame.K_f]:
        rnd_scalar -= 0.001

    # fps
    if ks[pygame.K_t]:
        fps += 1
    if ks[pygame.K_g]:
        fps -= 1

    # set / unset use of fps
    if ks[pygame.K_y]:
        use_clock = not use_clock

	# fix variable boundaries
    if layers < 0:
        layers = 0

    if rnd_scalar < 0:
        rnd_scalar = 0

    if circles_per_layer < 0:
        circles_per_layer = 0

    if fps < 0:
        fps = 0
    elif fps > fps_max:
        fps = fps_max

    # Fill the background with white
    screen.fill(color_background)

    # Draw
    #   i is current layer
    #   j is current circle
    # Polar coordiantes (r,θ) are used to calculate circle position,
    # then translated into cartesian coordinates (x,y) for drawing.
    for i in range(layers):
        layer_radius = min(screen_width,screen_height)/(layers + 1) * (i + 1)
        for j in range(circles_per_layer):
            θ = 2*math.pi * j / circles_per_layer
            θ += rnd_scalar * math.sin(random.uniform(0,2*math.pi))
            (x_rel,y_rel) = polar_to_cartesian(layer_radius,θ)
            pos = (x_rel + screen_width/2, y_rel + screen_height/2)

            pygame.draw.circle(screen, color_circle, pos, circle_radius)

    
    # Flip the display (execute the drawing to the screen)
    pygame.display.flip()

    # manage fps (only if use_clock is True)
    if use_clock:
        clock.tick(fps)

# Done! Time to quit.
pygame.quit()
