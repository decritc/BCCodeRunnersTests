import pygame
from pygame import *
import os
import clock

dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
bg = pygame.image.load(dir_path + '/windowtests/textured_background.jpg').convert()

pygame.display.set_caption('Magic Mirror')

clock_fps = pygame.time.Clock()


done = False
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord("q"):
                done = True

    screen.blit(bg, (0,0))

    clock_surface = Surface((300, 300))
    clock_surface.set_alpha(100)

    clock_surface.blit(clock.updateAndRender(), (0, 0))
    screen.blit(clock_surface, (20, 50))

    pygame.display.update()

    clock_fps.tick(30)

pygame.quit()

