'''
Maze Game
Loaded from a file.

Tasks:
1. Make the player visible in the maze. Hint: blit
2. Make the player move with the arrow keys.
3. Make the player stop when it hits a wall. In all directions.
4. Add objects to pick up. Use: chrystal_wall_lightmagenta.png
5. Make the player pick up the object when it collides with it.
6. Make the object disappear when the player picks it up.
7. Add score to the game. Show the score on the screen.
8. When all objects are picked up, show a message on the screen.
9. Add monsters that move around in the maze. 
   Random movement of your choice. Use: ogre_old.png
10. Game over if the player collides with a monster.

Extra tasks:
1. Show the doors in the maze.
2. If the player enters a door, the player is teleported to another door.
'''
import pygame


# --- Define helper functions
def get_one_colliding_object(object_1, objects):
    '''Returns the first object in the list of objects
    that collides with object_1.
    Returns None if no object collides.'''
    for object_2 in objects:
        obj_1_rect = pygame.Rect(object_1['x'], object_1['y'], object_1['image'].get_width(), object_1['image'].get_height())
        obj_2_rect = pygame.Rect(object_2['x'], object_2['y'], object_2['image'].get_width(), object_2['image'].get_height())
        if obj_1_rect.colliderect(obj_2_rect):
            return object_2
    return None

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection.
    '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# --- Initialize Pygame
pygame.init()

# --- Add elements to the game.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# load graphics
sand_image = pygame.image.load("pygame/floor_sand_stone_0.png")
wall_image = pygame.image.load("pygame/brick_brown_0.png")
#door "img/open_door.png"
player_image = pygame.image.load("pygame/deep_elf_knight_old.png")
player_radius = (player_image.get_width() + player_image.get_height()) / 4
pickup_image = pygame.image.load("pygame/crystal_wall_lightmagenta.png")
pickup_radius = (pickup_image.get_width() + pickup_image.get_height()) / 4
# Add visual elements to the game

enemy_image = pygame.image.load("pygame/ogre_old.png")

wall_size = wall_image.get_width()
walls = []

pickups = []

font = pygame.font.Font(None, 32)
text = font.render('score: 0',True, WHITE)
textRect = text.get_rect()
textRect.center = (450 // 2, 20)
textRect2 = text.get_rect()
textRect2.center = (450 // 2, 450 // 2)
score = 0
# Create the player
player = {}
player['image'] = player_image
player['speed'] = 4

# Read the maze from the file.

file = open('pygame/maze.txt', 'r')
line = file.readline()
maze_width = len(line) - 1  # Do not count the newline character.
maze_height = 0
x = 0
y = 0
while len(line) > 1:
    maze_height += 1
    for char in line:
        if char == 'x' or char == 'd':
            wall = {}
            wall['x'] = x
            wall['y'] = y
            wall['image'] = wall_image
            walls.append(wall)
        elif char == 'e':
            player['x'] = x
            player['y'] = y
        elif char == 'p':
            pickup = {}
            pickup['x'] = x
            pickup['y'] = y
            pickup['image'] = pickup_image
            pickups.append(pickup)

        x += wall_size
    x = 0
    y += wall_size
    line = file.readline()

file.close()

# --- Set the width and height of the screen [width, height]
size = (maze_width * wall_size, maze_height * wall_size)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Game")

# --- Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
is_running = True
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    # --- Game logic should go here
    # --- Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player['x'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] += player['speed']
    elif keys[pygame.K_RIGHT]:
        player['x'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] -= player['speed']
    elif keys[pygame.K_UP]:
        player['y'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] += player['speed']
    elif keys[pygame.K_DOWN]:
        player['y'] += player['speed']  
        if get_one_colliding_object(player, walls):
            player['y'] -= player['speed']
    else:
        # snap player to grid
        player['x'] = round(player['x'] / wall_size) * wall_size
        player['y'] = round(player['y'] / wall_size) * wall_size
    
    for pickup in pickups:
        if collides(player['x'], player['y'], player_radius, pickup['x'], pickup['y'], pickup_radius):
            pickups.remove(pickup)
            score = score + 1
            text = font.render('score: '+ str(score),True, WHITE)
    
    if score == 5:
        text2 = ('YOU WON!', True, WHITE)

    # --- Screen-clearing code goes here
    # fill with sand
    for y in range(0, size[1], wall_size):
        for x in range(0, size[0], wall_size):
            screen.blit(sand_image, (x, y))
    # --- Drawing code should go here
    for wall in walls:
        screen.blit(wall_image, (wall['x'], wall['y']))

    screen.blit(player_image, (player['x'], player['y']))

    screen.blit(enemy_image, enemy(['x'], enemy['y']))

    for pickup in pickups:
        screen.blit(pickup_image, (pickup['x'], pickup['y']))

    screen.blit(text, textRect)

    pygame.display.update()  # or pygame.display.flip()
    # --- Increase game time
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()