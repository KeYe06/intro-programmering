'''
Task

lägg till två egna texter
'''
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Show text")

# Add visual elements to the game
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 20)
text = font.render('Hello, World!', True, BLACK, WHITE)
text2 = font2.render('werwerwer', True, BLACK, GREEN)
text3 = font2.render('3333333333', True, GREEN, WHITE)
textRect = text.get_rect()
textRect.center = (700 // 2, 500 // 2)
textRect2 = text.get_rect()
textRect2.center = (400, 200)
textRect3 = text.get_rect()
textRect3.center = (700 // 2, 400)
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)
 
    # --- Drawing code should go here
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()