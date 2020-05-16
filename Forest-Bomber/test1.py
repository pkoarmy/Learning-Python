import pygame

# Initialize the game class
pygame.init()

# Create a canvas on which to display everything
# define width=640, height=480
window = (640,480)

# Let pygame that we are going to use this canvas
screen = pygame.display.set_mode(window)

# Create a surface with the same size as the window
background = pygame.Surface(window)

# Populate the surface with objects to be displayed
# Draw Rectangle on this background with colo Green+Blue
# start from x=20, y=20 and size with x=40, y=40
pygame.draw.rect(background,(0,255,255),(20,20,40,40))

# Draw Rectangle on this background with colo Red+Blue
# start from x=120, y=120 and size with x=50, y=50
pygame.draw.rect(background,(255,0,255),(120,120,50,50))

# Blit the surface onto the canvas ####
screen.blit(background,(0,0))

# Update the the display and wait
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
