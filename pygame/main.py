# Example file showing a basic pygame "game loop"
import pygame

# pygame setup and initiliaze pygame
pygame.init()
# Create the screen and set screen dimension
screen = pygame.display.set_mode((800, 600))


# set title and icon
pygame.display.set_caption('Space Invation.')
# load image for a window icon
icon_image = pygame.image.load('rocket-ship.png')
# store the image in the set icon method
pygame.display.set_icon(icon_image)

# CREATE PLAYER FOR THE GAME
# load image that will rapresent the player
img_player = pygame.image.load('player_img.png')

# since the image of the icon is extremely large we are going to chage its dimension
new_size = (75,75)
img_player = pygame.transform.scale(img_player, new_size)

# when setting coordinate always remmber The (0, 0) coordinates represent the top-left corner of the surface.
# establish the x, y coordinate that will move the plyaer around
# player starting point position.
player_x = 362.5
player_y = 525
# keep track of the player movements once the key are pressed
player_x_change = 0
player_y_change = 0

# create function that will display player position
def player(x, y):
    screen.blit(img_player, (x , y))




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
    background_rgb = (64, 224, 208) # Turquoise
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

    
    # update the player position in the while loop
    player(player_x, player_y)

    # update the screen properly
    pygame.display.update()
