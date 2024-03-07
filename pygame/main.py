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

# establish the x, y coordinate that will move the plyaer around
player_x = 362.5
player_y = 525

# create function that will display player
def player():
    screen.blit(img_player, (player_x, player_y))




# variable that will dictate the while loop condition
is_running = True

#  set game loop
while is_running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False 

    # all the update within the game must be done insided of the while loop
    # You will use rgb colors numbers to set the background of the screen, however you can also just name the color and pass it as a string
    background_color = "violet"
    background_rgb = (205,144,228)
    screen.fill(background_rgb)

    player()

     # flip() the display to put your work on screen
    pygame.display.update()
