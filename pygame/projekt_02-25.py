import pygame
import random
import time

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection.
    '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

BLACK = (255,255,255)
WHITE = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()


size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("peanits")

lives = 5
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
plum_x = snake_x
plum_y = snake_y

font = pygame.font.Font(None, 32)
text = font.render('Lives: 5',True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (1000 // 2, 50)

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

    cherry_speed = -5
    if (random.randint(0, 100) < 2):
        cherry_y = random.randint(0, 800)
        cherries.append([950, cherry_y, cherry_speed])

    for plum in plums:
        # Move plum
        plum[0] += plum[2]
    

    for cherry in cherries:
        if cherry[0] < 0:
            cherries.remove(cherry)
            lives = lives - 1
            text = font.render('Lives: '+ str(lives),True, BLACK, WHITE)
        cherry[0] += cherry[2]
        if collides(plum_x, plum_y, plum_radius, cherry[0], cherry[1], cherry_radius):
            cherries.remove(cherry)

    if lives == 0:
        done = True
        text = font.render('GAME OVER', True, BLACK, WHITE)

    screen.fill(WHITE)
    screen.blit(snake_image, [snake_x, snake_y])
    for plum in plums:
        screen.blit(plum_image, [plum[0], plum[1]])
    for cherry in cherries:
        screen.blit(cherry_image, [cherry[0], cherry[1]])
    screen.blit(text, textRect)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
done = False

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
