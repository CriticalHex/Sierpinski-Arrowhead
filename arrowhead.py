import pygame
from math import sin, cos, sqrt, pi


class Trapezoid:
    def __init__(self,x,y,scale,trapID):
        self.ID = trapID
        self.scale = scale
        if trapID == 1:
            self.p0x = x
            self.p0y = y
            self.p1x = scale * cos((5*pi)/3) + self.p0x
            self.p1y = scale * sin((5*pi)/3) + self.p0y
            self.p2x = self.p1x + scale
            self.p2y = self.p1y
            self.p3x = scale * cos((5*pi)/3) + self.p2x
            self.p3y = scale * sin((pi)/3) + self.p2y
        if trapID == 2:
            self.p0x = x
            self.p0y = y
            self.p1x = scale * cos((pi)/3) + self.p0x
            self.p1y = scale * sin((pi)/3) + self.p0y
            self.p2x = scale * cos((2*pi)/3) + self.p1x
            self.p2y = scale * sin((2*pi)/3) + self.p1y
            self.p3x = scale * cos(pi) + self.p2x
            self.p3y = scale * sin(pi) + self.p2y
        if trapID == 3:
            self.p0x = x
            self.p0y = y
            self.p1x = scale * cos((2*pi)/3) + self.p0x
            self.p1y = scale * sin((2*pi)/3) + self.p0y
            self.p2x = scale * cos((pi)/3) + self.p1x
            self.p2y = scale * sin((pi)/3) + self.p1y
            self.p3x = scale + self.p2x
            self.p3y = self.p2y
        self.points = [(self.p0x,self.p0y),(self.p1x,self.p1y),(self.p2x,self.p2y),(self.p3x,self.p3y)]
        self.color = (0,255,0)
            
    
    def draw(self):
        pygame.draw.aalines(screen,self.color,False,self.points)

    def expand(self):
        if self.ID == 1:
            traps2.append(Trapezoid(self.p1x,self.p1y,self.scale/2,2))
            traps2.append(Trapezoid(self.p1x,self.p1y,self.scale/2,1))
            traps2.append(Trapezoid(self.p2x,self.p2y,self.scale/2,3))
            return
        if self.ID == 2:
            traps2.append(Trapezoid(self.p3x,self.p3y,self.scale/2,1))
            traps2.append(Trapezoid(self.p1x,self.p1y,self.scale/2,2))
            traps2.append(Trapezoid(self.p0x,self.p0y,self.scale/2,3))
        if self.ID == 3:
            traps2.append(Trapezoid(self.p0x,self.p0y,self.scale/2,2))
            traps2.append(Trapezoid(self.p1x,self.p1y,self.scale/2,3))
            traps2.append(Trapezoid(self.p2x,self.p2y,self.scale/2,1))

pygame.init()

pygame.display.set_caption("ArrowHead")
screen = pygame.display.set_mode((1920, 1080))
screen.fill((0,0,0))
Running = True

traps = [Trapezoid(600,800,400,1)]
traps2 = []
count = 0

open = False

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            Running = False
        if keys[pygame.K_SPACE]:
            open = True
            count += 1

    screen.fill((0,0,0))
    
    for trap in traps:
        trap.draw()
        if open:
            trap.expand()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            Running = False
            break
        pygame.display.flip()
    if open:
        traps = traps2.copy()
        traps2.clear()
        open = False

    #pygame.display.flip()