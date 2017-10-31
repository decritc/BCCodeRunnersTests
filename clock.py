import pygame, time, math
from pygame import Surface


BRIGHTBLUE = (  0,  50, 255)
WHITE      = (255, 255, 255)
DARKRED    = (128,   0,   0)
RED        = (204,  52,   0)
YELLOW     = (255, 255,   0)
BLACK      = (  0,   0,   0)

HOURHANDCOLOR = DARKRED
MINUTEHANDCOLOR = RED
SECONDHANDCOLOR = BLACK

WINDOWWIDTH = 300
WINDOWHEIGHT = 300
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)


CLOCKNUMSIZE = 50
CLOCKSIZE = 120


def getTickPosition(tick, stretch=1.0, originx=WIN_CENTERX, originy=WIN_CENTERY):

    tick -= 15
    tick = tick % 60
    tick = 60 - tick

    x = math.cos(2 * math.pi * (tick / 60.0))
    y = -1 * math.sin(2 * math.pi * (tick / 60.0))

    x *= stretch
    y *= stretch

    x += originx
    y += originy

    return x, y


def updateAndRender():
    clock_surface = Surface((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.font.init()
    fontObj = pygame.font.SysFont('Roboto', CLOCKNUMSIZE)

    clock_surface.fill(BRIGHTBLUE)

    for i in range(1, 13):
        clockNumSurfs = fontObj.render('%s' % i, True, BLACK)
        clockNumRect = clockNumSurfs.get_rect()
        clockNumRect.center = getTickPosition(i * 5, CLOCKSIZE)
        clock_surface.blit(clockNumSurfs, clockNumRect)

    now = time.localtime()
    now_hour = now[3] % 12
    now_minute = now[4]
    now_second = now[5] + (time.time() % 1)

    x, y = getTickPosition(now_hour * 5 + (now_minute * 5 / 60.0), CLOCKSIZE * 0.6)
    pygame.draw.line(clock_surface, HOURHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 8)

    x, y = getTickPosition(now_minute + (now_second / 60.0), CLOCKSIZE * 0.8)
    pygame.draw.line(clock_surface, MINUTEHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 6)

    x, y = getTickPosition(now_second, CLOCKSIZE * 0.9)
    pygame.draw.line(clock_surface, SECONDHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 2)

    x, y = getTickPosition(now_second, CLOCKSIZE * -0.2)
    pygame.draw.line(clock_surface, SECONDHANDCOLOR, (WIN_CENTERX, WIN_CENTERY), (x, y), 2)

    pygame.draw.rect(clock_surface, BLACK, (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)

    return clock_surface
