# Example file showing a basic pygame "game loop"
import pygame, random

# pygame setup and initiliaze pygame
pygame.init()
# Create the screen and set screen dimension
screen = pygame.display.set_mode((800, 600))


# set title and icon, load image for a window icon, store the image in to be displayed on the screen 
pygame.display.set_caption('Space Invation')
game_icon = pygame.image.load('rocket-ship.png')
pygame.display.set_icon(game_icon)

# CREATE PLAYER FOR THE GAME
# load image that will rapresent the player
img_player = pygame.image.load('player_img.png')

# set hight/width so the img can render properly on the screen
player_size = (75,75)
img_player = pygame.transform.scale(img_player, player_size)

# when setting coordinate always remmber The (0, 0) coordinates represent the top-left corner of the surface.
# player coordinate starting position
player_x = 362.5
player_y = 450

# keep track of the player movements once the key are pressed
player_x_change = 0
player_y_change = 0

def player_position(x, y):
    """This method will take the x and y axis the coordinates and display the player position on the screen
    """
    screen.blit(img_player, (x , y))

# CREATE ENEMY

# upload image
img_enemy = pygame.image.load('enemy_player.png')
# allocate width and height 
enemy_size = (60,60)
# assign the dimension to the enemy img
img_enemy = pygame.transform.scale(img_enemy, enemy_size)
# In case you habe an image that is not facing the player go ahead and use the pygame rotate function to 180
# img_enemy = pygame.transform.rotate(img_enemy, 180)
# set the base coordinates for the enemy player
# enemy_x = 362.5
# enemy_y = 0

# set the enemy position in a random spot
enemy_x = random.randint(0, 740)
enemy_y = random.randint(0, 200)
enemy_x_change = 0.15
enemy_y_change = 50

def enemy_position(x,y):
    """This method will take the x and y axis the coordinates and display the enemy position on the screen
    """
    screen.blit(img_enemy, (x,y))


# functions to handle screen restrictions
def x_axis_restriction(p_x):
    """method to handle x-axis screen restriction"""
    if p_x <= 0:
        p_x = 0
    elif p_x >= 725:
        p_x = 725
    return p_x

def y_axis_restriction(p_y):
    """method to handle y-axis screen restriction"""
    if p_y <= 0:
        p_y = 0
    elif p_y >= 525:
        p_y = 525
    return p_y

# def x_axis_enemy_movement(e_x, e_x_change, e_y, e_y_change):
#     if e_x <= 0:
#         e_x_change = 0.3
#         e_y += e_y_change
#     elif e_x >= 725:
#         e_x_change = -0.3
#         e_y += e_y_change
#     return e_x_change, e_y

# Let's load the background with an outerspace image:
background_img = pygame.image.load('background_img.png')

background_img = pygame.transform.scale(background_img, (800,600))

# variable that will dictate the while loop condition
is_running = True

#  set game loop
while is_running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        # closing events
        if event.type == pygame.QUIT:
            is_running = False

        # Controlling the direction of the rocket with our key board
        # remeber everything is an event and we will program as such
        
        # press arrow key event 
        if event.type == pygame.KEYDOWN:
            # handles the x-axis movements 
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            elif event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            # handle the y-axis movement
            elif event.key == pygame.K_UP:
                player_y_change = -0.3
            elif event.key == pygame.K_DOWN:
                player_y_change = 0.3

    
        
        # release key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0



    # all the update within the game must be done insided of the while loop
    # You will use rgb colors numbers to set the background of the screen, however you can also just name the color and pass it as a string
    background_color = "violet"
    background_rgb = (229, 204, 255) # Turquoise
    # screen.fill(background_rgb)
    # value that will move the player up or down depending on which axis you're manipulating with
    # player_x += 0.1
    # player_y -= 0.1
    screen.blit(background_img, (0,0))

    # modify player position based on keys being pressed
    player_x += player_x_change
    player_y += player_y_change

    # ensure the player image stays within the screen
    player_x = x_axis_restriction(player_x)
    player_y = y_axis_restriction(player_y)

    # Modify enemy location
    enemy_x += enemy_x_change
    # set enemy position
    # enemy_x_change, enemy_y = x_axis_enemy_movement(enemy_x, enemy_x_change, enemy_y, enemy_x_change)
    
    if enemy_x <= 0:
        enemy_x_change = 0.15
        enemy_y += enemy_y_change
    elif enemy_x >= 740:
        enemy_x_change = -0.15
        enemy_y += enemy_y_change

    # update the player/enemy position in the while loop
    player_position(player_x, player_y)
    enemy_position(enemy_x, enemy_y)

    # update the screen properly
    pygame.display.update()


