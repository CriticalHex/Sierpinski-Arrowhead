import pygame
from math import sin, cos, sqrt, pi


class Trapezoid:
    def __init__(self):
        pass


pygame.init()

pygame.display.set_caption("ArrowHead")
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
    line1 = (200 * cos((5*pi)/3) + startx, 200 * sin((5*pi)/3) + starty)
    line2 = (line1[0] + 200,line1[1])
    line3 = (200 * cos((5*pi)/3) + line2[0],200 * sin((pi)/3) + line2[1])
    print(line1,line2,line3)
    pygame.draw.aalines(screen, (0,255,0), False, [(startx,starty),line1,line2,line3])

    pygame.display.flip()