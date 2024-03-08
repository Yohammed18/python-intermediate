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
player_y = 525

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
enemy_size = (75,75)
# assign the dimension to the enemy img
img_enemy = pygame.transform.scale(img_enemy, enemy_size)
# In case you habe an image that is not facing the player go ahead and use the pygame rotate function to 180
# img_enemy = pygame.transform.rotate(img_enemy, 180)
# set the base coordinates for the enemy player
# enemy_x = 362.5
# enemy_y = 0

# set the enemy position in a random spot
enemy_x = random.randint(0, 725)
enemy_y = random.randint(0, 200)

def enemy_position(x,y):
    """This method will take the x and y axis the coordinates and display the enemy position on the screen
    """
    screen.blit(img_enemy, (x,y))



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
    screen.fill(background_rgb)
    # value that will move the player up or down depending on which axis you're manipulating with
    # player_x += 0.1
    # player_y -= 0.1


    # set the coordinate of the player on the x,y axis when the user press on the up, down, left or right key
    player_x += player_x_change
    player_y += player_y_change

    # set limits so it doesn't escap window 
    if player_x <= 0:
        player_x = 0
    elif player_x >= 725:
        player_x = 725

    if player_y <= 0:
        player_y = 0
    elif player_y >= 525:
        player_y = 525

    
    # update the player/enemy position in the while loop
    player_position(player_x, player_y)
    enemy_position(enemy_x, enemy_y)

    # update the screen properly
    pygame.display.update()
