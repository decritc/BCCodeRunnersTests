import pygame, time, math
from pygame import Surface

WINDOWWIDTH = 300
WINDOWHEIGHT = 300

clock_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))
last_y = 150
first_run = True

def updateAndRender():
    global first_run
    global last_y
    x = 250

    if first_run:
        clock_surface.fill((0, 50, 255))

    now = time.localtime()
    now_second = now[5] + (time.time() % 1)
    y = (3 * math.sin(now_second)) + last_y
    clock_surface.scroll(-2, 0)

    if y > 300 or y < 0:
        y = 150

    pygame.draw.line(clock_surface, (0, 0, 0), (x, y + 4), (x,y), 4)

    first_run = False
    last_y = y

    return clock_surface
