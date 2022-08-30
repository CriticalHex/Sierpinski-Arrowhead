import pygame
from math import sin, cos, sqrt


class Trapezoid:
    def __init__(self):
        pass


pygame.init()

pygame.display.set_caption("Wave Function Collapse")
screen = pygame.display.set_mode((1920, 1080))
screen.fill((0,0,0))
Running = True

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        Running = False

    screen.fill((0,0,0))
    
    startx = 500
    starty = 500
    line1 = (10 * cos(60) + startx, 200 * sin(60) + starty)
    line2 = (10 * cos(60) + line1[0],200 * sin(60) + line1[1])
    line3 = (10 * cos(60) + line2[0],200 * sin(60) + line2[1])
    pygame.draw.aalines(screen, (0,255,0), False, [(startx,starty),line1,line2,line3])

    pygame.display.flip()