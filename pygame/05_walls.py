'''
Demo collision detection between a bird and a box

Tasks:

1. Make it possible for the bird to move in all directions.
2. Make is impossible for the bird to move outside the screen.
3. Check that the box goes red when it collides with the bird.
4. Make it impossible for the bird to move into the box. 
   Hint: Move the bird back to its previous position.
5. Add a second box to the game.
6. Make it impossible for the bird to move into the second box.
7. Which changes do you need to make if you want to add another ten boxes to the game?
'''

import pygame

# Define colors.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

# Initialize all imported pygame modules.
pygame.init()

# Set the width and height of the screen [width, height].
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Collision with Walls")

# --- Add visual elements to the game.
# Bird
bird_image = pygame.image.load("pygame/pelican.png")
bird_x = 0
bird_y = 0

# Box
# Green but red when there is a collision.
box = pygame.Rect(100, 100, 200, 200)
box2 = pygame.Rect(400, 300, 200, 200)
box_color = GREEN

is_running = True
# Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    # --- Game logic should go here
    # Move the bird with the arrow keys.
    
    # ... Write code here ....

    # Check for collision between the bird and the box.
    if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))) or box2.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
        box_color = RED
        bird_x = 500
        bird_y = 100
    else:
        box_color = GREEN

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y += -5
    if keys[pygame.K_DOWN]:
        bird_y += 5
    if keys[pygame.K_LEFT]:
        bird_x += -5
    if keys[pygame.K_RIGHT]:
        bird_x += 5
    
    if bird_x < 0:
        bird_x = 0
    if bird_x > 750:
        bird_x = 750
    if bird_y > 550:
        bird_y = 550
    if bird_y < 0:
        bird_y = 0

    # --- Screen-clearing code goes here
    screen.fill(SKY_BLUE)
    # --- Drawing code should go here
    screen.blit(bird_image, (bird_x, bird_y))
    pygame.draw.rect(screen, box_color, box)
    pygame.draw.rect(screen, box_color, box2)
    pygame.display.update()  # or pygame.display.flip()
    # --- Increase game time
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()