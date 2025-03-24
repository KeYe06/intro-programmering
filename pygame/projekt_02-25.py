import pygame
import random

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
pygame.display.set_caption("space invanders")

lives = 5
snake_image = pygame.image.load("pygame/snake.png")
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygame.image.load("pygame/plum.png")
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4
plums = []

cherry_image = pygame.image.load("pygame/ogre_old.png")
cherries = []
cherry_radius = (cherry_image.get_width() + cherry_image.get_height()) / 4

ammo_image = pygame.image.load("pygame/ammo.png")
ammo_radius = (ammo_image.get_width() + ammo_image.get_height()) / 4
ammos = []

snake_x = 30
snake_y = 700
snake_last_direction = "right"
plum_x = 0
plum_y = 0

score = 0

font = pygame.font.Font(None, 45)
text = font.render('Lives: 5',True, BLACK, WHITE)
text2 = font.render('Ammo: 10', True, BLACK, WHITE)
text3 = font.render('Score: 0', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (1000 // 2, 50)
textRect2 = text.get_rect()
textRect2.center = (70, 770)
textRect3 = text.get_rect()
textRect3.center = (1000 // 2, 100)

done = False
clock = pygame.time.Clock()

time_to_shoot = 0
reload = 0
ammo = 5
switch = 3
switch2 = 3
stage1 = 20


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
    if keys[pygame.K_SPACE] and time_to_shoot <= 0 and reload <= 0:
        plum_x = snake_x
        plum_y = snake_y
        plum_speed = 18
        plums.append([plum_x, plum_y, plum_speed]) # x, y, speed
        ammo = ammo - 1
        text2 = font.render('Ammo: '+ str(ammo), True, BLACK, WHITE)
        time_to_shoot = 0.18 #sekunder

    if snake_y < 0:
        snake_y = 0
    if snake_y > 750:
        snake_y = 750

    if ammo == 0:
        reload = 0.9
        if keys[pygame.K_SPACE]:
            ammo = ammo + 5
            text2 = font.render('Reloading....', True, BLACK, WHITE)
    if reload <= 0:
        text2 = font.render('Ammo: '+ str(ammo), True, BLACK, WHITE)

    if stage1 > 0:
        cherry_speed = -5
        if (random.randint(0, 130) < 2):
                cherry_y = random.randint(0, 750)
                cherry_x = 950
                cherries.append([cherry_x, cherry_y, cherry_speed])

    if stage1 <= 0:
        cherry_speed = -7
        switch = 2
        if switch > 0:
            switch2 = 2
            cherry_y += 5
        elif switch2 > 0:
            switch2 = 1
            cherry_y += -5
        if (random.randint(0, 110) < 2):
                cherry_y = random.randint(0, 750)
                cherry_x = 950
                cherries.append([cherry_x, cherry_y, cherry_speed])

                #SKAPA DICTIONARIES
    
    ammo_speed = -5
    if (random.randint (0, 250) < 1):
        ammo_y = random.randint(0,750)
        ammo_x = 950
        ammos.append([ammo_x, ammo_y, ammo_speed])

    for plum in plums:
        # Move plum
        plum[0] += plum[2]

    for cherry in cherries:
        if cherry[0] < 0:
            cherries.remove(cherry)
            lives = lives - 1
            text = font.render('Lives: '+ str(lives),True, BLACK, WHITE)
        cherry[0] += cherry[2]
        for plum in plums:
            if collides(plum[0], plum[1], plum_radius, cherry[0], cherry[1], cherry_radius):
                cherries.remove(cherry)
                score += 100
                text3 = font.render('Score: ' + str(score), True, BLACK, WHITE)
                break
    
    for ammon in ammos:
        if ammon[0] < 0:
            ammos.remove(ammon)
        ammon[0] += ammon[2]
        if collides(snake_x, snake_y, snake_radius, ammon[0], ammon[1], ammo_radius):
            ammos.remove(ammon)
            ammo += 10

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
    screen.blit(text2, textRect2)
    screen.blit(text3,textRect3)
    for ammon in ammos:
        screen.blit(ammo_image, [ammon[0], ammon[1]])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    time_to_shoot -= 1.0/60
    reload -= 1.0/60
    stage1 -= 1.0/60
    switch -= 1.0/60

done = False

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
