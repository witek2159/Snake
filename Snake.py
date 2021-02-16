# import the pygame module, so you can use it
import time
import pygame, sys
from pygame.locals import *

#snake segment class
class Segment:
    Xpos = 0
    Ypos = 0

    def __init__(self,X,Y):
        self.Xpos = X
        self.Ypos = Y
    
    def draw(self,screen):
        pygame.draw.rect(screen,(100,100,100),(self.Xpos,self.Ypos,50,50))

    def update(self,X,Y):
        self.Xpos = X
        self.Ypos = Y


#snake class
class Snake:
    SEG = Segment
    Xpos = 0
    Ypos = 0
    direction = 'D'

    def __init__(self,X,Y):
        self.Xpos = X
        self.Ypos = Y
        self.SEG = Segment(X,Y)

    def draw(self,screen):
        self.SEG.draw(screen)

    def update(self):
        if self.direction == 'R':
            self.SEG.update(self.SEG.Xpos+50+10,self.SEG.Ypos)
        if self.direction == 'L':
            self.SEG.update(self.SEG.Xpos-50-10,self.SEG.Ypos)
        if self.direction == 'U':
            self.SEG.update(self.SEG.Xpos,self.SEG.Ypos-50-10)
        if self.direction == 'D':
            self.SEG.update(self.SEG.Xpos,self.SEG.Ypos+50+10)

    def change_direction(self,d):
        self.direction = d


# define a main function
def main():
    
     
    # initialize the pygame module
    pygame.init()
    # set caption
    pygame.display.set_caption("Snake v. 0.0.1")

     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((490,490))

    SNK = Snake(10,10) 
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        #fill screen with white color
        screen.fill((255,255,255))
        #update screen
        SNK.draw(screen)  
        SNK.update()    
        pygame.display.update()
        time.sleep(1)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    SNK.change_direction('U')
                if event.key == K_s:
                    SNK.change_direction('D')
                if event.key == K_a:
                    SNK.change_direction('L')
                if event.key == K_d:
                    SNK.change_direction('R')
  
main()