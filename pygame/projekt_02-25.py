import pygame
import random

BLACK = (255,255,255)
WHITE = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()

size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("peanits")

snake_image = pygame.image.load("pygame/snake.png")
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4
plum_image = pygame.image.load("pygame/plum.png")
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4
plums = []
cherry_image = pygame.image.load("pygame/cherries.png")
cherries = []
cherry_radius = (cherry_image.get_width() + cherry_image.get_height()) / 4
snake_x = 30
snake_y = 700
snake_last_direction = "right"

done = False
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_y -= 7
    if keys[pygame.K_DOWN]:
        snake_y += 7
    if keys[pygame.K_SPACE]:
        plum_x = snake_x
        plum_y = snake_y
        plum_speed = 10
        if snake_last_direction == "left":
            plum_speed = -10
        plums.append([plum_x, plum_y, plum_speed]) # x, y, speed

    cherry_speed = -10
    if (random.randint(0, 100) < 1):
        cherry_y = random.randint(0, 800)
        cherries.append([950, cherry_y, cherry_speed])

    for plum in plums:
        # Move plum
        plum[0] += plum[2]
    

    for cherry in cherries:
        if cherry[0] < 0:
            cherries.remove(cherry)
        cherry[0] += cherry[2]


    screen.fill(WHITE)
    screen.blit(snake_image, [snake_x, snake_y])
    for plum in plums:
        screen.blit(plum_image, [plum[0], plum[1]])
    for cherry in cherries:
        screen.blit(cherry_image, [cherry[0], cherry[1]])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
