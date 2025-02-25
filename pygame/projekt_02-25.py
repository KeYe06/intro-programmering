import pygame
import random

BLACK = (255,255,255)
WHITE = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()

snake_image = pygame.image.load("pygame/snake.png")

done = False

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


screen.fill(BLACK)