# import the pygame module, so you can use it
import time
import random
import pygame, sys
from pygame.locals import *

# define a variable to control the main loop
running = True

Movment_Flag = True

SEG_size = 25
SEG_spacing = 5

# define qiut function
def quit():
    # change the value to False, to exit the main loop
    running = False
    pygame.quit()
    sys.exit()

#define food class
class Food:
    Xpos = 0
    Ypos = 0

    def __init__(self):
        randx = random.randint(0,17)
        randy = random.randint(0,17)
        self.Xpos = (randx * 25) + (randx * 5)
        self.Ypos = (randy * 25) + (randy * 5)

    def draw(self,screen):
        pygame.draw.rect(screen,(250,0,0),(self.Xpos,self.Ypos,SEG_size,SEG_size))

    def food_eaten(self):
        randx = random.randint(0,17)
        randy = random.randint(0,17)
        self.Xpos = (randx * 25) + (randx * 5)
        self.Ypos = (randy * 25) + (randy * 5)

FOOD = Food()

#snake segment class
class Segment:
    Xpos = 0
    Ypos = 0
    Last_Xpos = 0
    Last_Ypos = 0

    def __init__(self,X,Y):
        self.Xpos = X
        self.Ypos = Y

    
    def draw(self,screen):
        pygame.draw.rect(screen,(100,100,100),(self.Xpos,self.Ypos,SEG_size,SEG_size))

    def update(self,X,Y):
        self.Last_Xpos = self.Xpos
        self.Last_Ypos = self.Ypos

        self.Xpos = X
        self.Ypos = Y


#snake class
class Snake:
    Alive = True
    SEG = []
    Xpos = 0
    Ypos = 0
    direction = 'D'
    Snake_length = 1

    def __init__(self,X,Y):
        
        self.Xpos = X
        self.Ypos = Y
        for i in range(self.Snake_length):
            if i == 0:
                self.SEG.append(Segment(X,Y))
            else:
                self.SEG.append(Segment(-SEG_size,-SEG_size))
        
    def draw(self,screen):
        for i in range(self.Snake_length):
            self.SEG[i].draw(screen)

    def update(self):
        #move snake head in set direction
        if self.direction == 'R':
            self.SEG[0].update(self.SEG[0].Xpos+SEG_size+SEG_spacing,self.SEG[0].Ypos)
        if self.direction == 'L':
            self.SEG[0].update(self.SEG[0].Xpos-SEG_size-SEG_spacing,self.SEG[0].Ypos)
        if self.direction == 'U':
            self.SEG[0].update(self.SEG[0].Xpos,self.SEG[0].Ypos-SEG_size-SEG_spacing)
        if self.direction == 'D':
            self.SEG[0].update(self.SEG[0].Xpos,self.SEG[0].Ypos+SEG_size+SEG_spacing)
        #move snake body
        for i in range(self.Snake_length-1):
            self.SEG[i+1].update(self.SEG[i].Last_Xpos,self.SEG[i].Last_Ypos)
        #check for colision with map border
            if self.SEG[0].Xpos+SEG_size > 505 or self.SEG[0].Xpos+SEG_size < 0 or self.SEG[0].Ypos+SEG_size > 505 or self.SEG[0].Ypos+SEG_size < 0:
                self.Alive = False
        #check for colision with itself
            for i in range(self.Snake_length-1):
                if self.SEG[0].Xpos == self.SEG[i+1].Xpos and self.SEG[0].Ypos == self.SEG[i+1].Ypos:
                    self.Alive = False

    def food_check(self,fx,fy):
        if self.SEG[0].Xpos == fx and self.SEG[0].Ypos == fy:
            self.SEG.append(Segment(-SEG_size,-SEG_size))
            self.Snake_length += 1
            FOOD.food_eaten()

    def change_direction(self,d):
        self.direction = d


# define a main function
def main():
    
     
    # initialize the pygame module
    pygame.init()
    # set caption
    pygame.display.set_caption("Snake v. 0.0.4")

     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((505,505))

    SNK = Snake(0,0) 

    # main loop
    delay = 0
    while running:
        if delay == 100000:
            Movment_Flag = True
            delay = 0
            #fill screen with white color
            if SNK.Alive == False:
                quit()
            screen.fill((255,255,255))
            #update screen
            FOOD.draw(screen)
            SNK.draw(screen)  
            SNK.update()   
            SNK.food_check(FOOD.Xpos,FOOD.Ypos) 
            pygame.display.update()
        else:
            delay +=1

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                quit()

            #set movment direction   
            if event.type == pygame.KEYDOWN:
                if event.key == K_w and Movment_Flag:
                    SNK.change_direction('U')
                    Movment_Flag = False
                elif event.key == K_s and Movment_Flag:
                    SNK.change_direction('D')
                    Movment_Flag = False
                elif event.key == K_a and Movment_Flag:
                    SNK.change_direction('L')
                    Movment_Flag = False
                elif event.key == K_d and Movment_Flag:
                    SNK.change_direction('R')
                    Movment_Flag = False
  
main()