# Example file showing a basic pygame "game loop"
import pygame, random, math
from pygame import mixer
# pygame setup and initiliaze pygame and backgourg music
pygame.init()
mixer.init()
# Create the screen and set screen dimension
screen = pygame.display.set_mode((800, 600))


# set title and icon, load image for a window icon, store the image in to be displayed on the screen 
pygame.display.set_caption('Space Invation')
game_icon = pygame.image.load('img\\rocket-ship.png')
pygame.display.set_icon(game_icon)


# load the music for the background of the game
mixer.music.load("sound\\background_space.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# CREATE PLAYER FOR THE GAME
# load image that will rapresent the player
img_player = pygame.image.load('img\\player_img.png')

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

# # upload image
# img_enemy = pygame.image.load('enemy_player.png')
# # allocate width and height 
# enemy_size = (60,60)
# # assign the dimension to the enemy img
# img_enemy = pygame.transform.scale(img_enemy, enemy_size)
# # set the enemy position in a random spot
# enemy_x = random.randint(0, 740)
# enemy_y = random.randint(0, 200)
# enemy_x_change = 0.5
# enemy_y_change = 50


# BUILD MULTIPLE ENEMIES 
# upload image
img_enemy = []
# allocate width and height 
enemy_size = (60,60)

# set the enemy position in a random spot
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 8

# create multiple enemies
for e in range(number_of_enemies):
    enemy = pygame.image.load('img\\enemy_player.png')
    enemy = pygame.transform.scale(enemy, enemy_size)
    img_enemy.append(enemy)
    enemy_x.append(random.randint(0, 740))
    enemy_y.append(random.randint(0, 200))
    enemy_x_change.append(0.5)
    enemy_y_change.append(50)

def enemy_position(x,y, en):
    """This method will take the x and y axis the coordinates and display the enemy position on the screen
    """
    screen.blit(img_enemy[en], (x,y))

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
background_img = pygame.image.load('img\\background_img.png')
background_img = pygame.transform.scale(background_img, (800,600))

# let's load bullet img and set coordinates and rotate the image to face up
img_bullet = pygame.image.load('img\\bullet_img.png')
bullet_size = (10,5)
img_bullet = pygame.transform.scale(img_bullet, bullet_size)
img_bullet = pygame.transform.rotate(img_bullet, 90)
# img_bullet = pygame.transform.scale(img_bullet, (10,10))

# bullet variables
bullet_x = 0
bullet_y = player_y

bullet_x_change = 0
bullet_y_change = 1.7 # bullet speed
visibile_bullet = False

# create a function to handle the bullet visibility
def shoot_bullet(x, y):
    global visibile_bullet
    visibile_bullet = True
    screen.blit(img_bullet, (x+35,y+10))

# calculate colision in gaming  
    # d= srt(x2−x1)^2 + (y2−y1)^2
def is_there_collision(x_1, y_1, x_2, y_2):
    """function utilized to detect if there is collision in the game """
    distance = math.sqrt(math.pow(x_1 - x_2, 2)+ math.pow(y_1 - y_2, 2))

    if distance < 27:
        return True
    else:
        False


# variable that will dictate the while loop condition
is_running = True

# Score variable
score = 0
my_font = pygame.font.Font('font\Montague.ttf',40)
text_x = 10
text_y = 10

def show_score(x,y):
    """show score on the screen"""
    text = my_font.render(f'Score: {score}', True, (224,224,224))
    screen.blit(text, (x,y))

# end of game text
end_font = pygame.font.Font('font\Broad_Casting.ttf', 80)

def final_text():
    my_final_font = end_font.render('GAME OVER', True, (255,255,255))
    screen.blit(my_final_font, (200,200))




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
        
        # press key event 
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
            elif event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('sound\\space_missile.mp3')
                bullet_sound.set_volume(.2)
                bullet_sound.play()
                if not visibile_bullet:
                    bullet_x = player_x
                    bullet_y = player_y 
                    shoot_bullet(bullet_x, bullet_y)
        
        # release key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0 


    # You will use rgb colors numbers to set the background of the screen, however you can also just name the color and pass it as a string
    background_color = "violet"
    background_rgb = (229, 204, 255) # Turquoise
    # screen.fill(background_rgb)
    screen.blit(background_img, (0,0))

    # modify player position based on keys being pressed
    player_x += player_x_change
    player_y += player_y_change

    # ensure the player image stays within the screen
    player_x = x_axis_restriction(player_x)
    player_y = y_axis_restriction(player_y)

     # Modify enemy location
    for enem in range(number_of_enemies):
        # end of game
        if enemy_y[enem] > 500:
            for k in range(number_of_enemies):
                enemy_y[k] = 1000
            
            final_text()
            break

        enemy_x[enem]+= enemy_x_change[enem]
        # set enemy position
        # enemy_x_change, enemy_y = x_axis_enemy_movement(enemy_x, enemy_x_change, enemy_y, enemy_x_change)
        if enemy_x[enem] <= 0:
            enemy_x_change[enem] = 0.15
            enemy_y[enem] += enemy_y_change[enem]
        elif enemy_x[enem] >= 740:
            enemy_x_change[enem] = -0.15
            enemy_y[enem] += enemy_y_change[enem]

        is_collision = is_there_collision(enemy_x[enem], enemy_y[enem], bullet_x, bullet_y)

        if is_collision:
            collision_sound = mixer.Sound('sound\\enemy_destroyed.mp3')
            collision_sound.set_volume(.7)
            collision_sound.play()
            bullet_y = player_y
            visibile_bullet = False
            score+= 1
            # set the enemy coordinate to re-appear else where when it hits
            enemy_x[enem] = random.randint(0, 740)
            enemy_y[enem] = random.randint(0, 200)
        
        enemy_position(enemy_x[enem], enemy_y[enem], enem)

    
    # update the player/enemy position in the while loop
    player_position(player_x, player_y)


    # bullet movement
    if bullet_y <= -10 or not visibile_bullet:
        visibile_bullet = False
        
    if visibile_bullet:
        """In this modification, the bullet's position is updated independently based on its own bullet_y coordinate. This should prevent the bullet from following the player after it's fired.
        """
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    show_score(text_x, text_y)

    # update the screen properly
    pygame.display.update()


