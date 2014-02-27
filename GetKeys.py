import time
import os
import sys
import pygame

#print ('Hello World')
pygame.init()
Running = True

screen = pygame.display.set_mode([50,50])

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_LEFT:
                print('l')

pygame.quit()
