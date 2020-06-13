import pygame
import time
x=0
pygame.init()
 
window = (640,480)
 
screen = pygame.display.set_mode(window)
 
background = pygame.Surface(window)
while x<=1000:
   pygame.time.delay(10)
   pygame.draw.rect(background, (0, 0, 0), pygame.Rect(20,100,80+x,100))
   pygame.draw.rect(background, (96, 85, 154), pygame.Rect(20,100,80+x,100))
   x+=10
 
 
 
 
 
screen.blit(background,(0,0))
 
pygame.display.flip()
done = False
while not done:
   pygame.time.delay(10)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True
 
pygame.quit()
 

