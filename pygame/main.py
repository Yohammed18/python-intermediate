# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
# set the game screen visual with height and width
screen = pygame.display.set_mode((800, 600))
# This creates a Clock object. The Clock object is used to control the timing of the game loop, ensuring that the game runs at a consistent frame rate. 
clock = pygame.time.Clock()
is_running = True

while is_running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False 

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

# this will allow the user to exit the game when they click on the exit bottom
pygame.quit()