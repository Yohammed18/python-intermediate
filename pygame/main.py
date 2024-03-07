# Example file showing a basic pygame "game loop"
import pygame

# pygame setup and initiliaze pygame
pygame.init()
# Create the screen and set screen dimension
screen = pygame.display.set_mode((500, 500))


# set title and icon
pygame.display.set_caption('Space Invation.')
# load image for a window icon
icon_image = pygame.image.load('rocket-ship.png')
# store the image in the set icon method
pygame.display.set_icon(icon_image)

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

     # flip() the display to put your work on screen
    pygame.display.update()
