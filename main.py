# import match_module as m
# from utils.match_module import (
#     add, mul, count, random
# )
#

from utils.match_module import  add, mul
from utils.string_module import  reverse_string, shout



# print(add(1,2))
# print(mul(2,3))
# print(reverse_string('hello'))
# print(shout('hello'))
# print(count)
# print(random.randint(1,4))


import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()