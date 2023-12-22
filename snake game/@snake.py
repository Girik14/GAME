import pygame
from pygame import *
import time
import random


pygame.init()
red =(255,0,0)
blue=(51,153,255)
grey =(192,192,192)
green=(51,102,0)
yellow=(0,255,255)


win_width=600
win_height=400
window=pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("snake Game")
time.sleep(5)

snake =10
snake_speed=15

clock=pygame.time.Clock()

font_style=pygame.font.SysFont("calibri",26)
score_font=pygame.font.SysFont("comicsansms",30)

def message(msg, color):
    msg= font_style.render(msg,True,color)
    window.blit(msg,[win_width/12,win_height/3])
    
    
def user_score(score):
    number = score_font.render("Score :"+str(score),True,red)
    window.blit(number,[0,0])
    
def game_snake(snake,snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window,green,[x[0],x[1],snake,snake])
        
def game_loop():
    gameover=False
    gameclose=False
 
    x1=win_width/2
    y1=win_height/2
    
    x1_change=0
    y1_change=0

    snake_length_list=[]
    snake_length=1
    
    foodx=round(random.randrange(0,win_width - snake)/10.0)*10.0
    foody=round(random.randrange(0,win_height - snake)/10.0)*10.0

    while not gameover:
        
        
        while gameclose==True:
            window.fill(grey)
            message ("you lost !! press P to play again and Q to Quit",red)
            user_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_p:
                     game_loop()
                  if event.key == pygame.K_q:
                     gameover=True
                     gameclose=False
                     
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change=-snake
                    y1_change=0
                if event.key == pygame.K_RIGHT:
                    x1_change=snake
                    y1_change=0
                if event.key == pygame.K_UP:
                    x1_change=0
                    y1_change=-snake
                if event.key == pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake

        if x1>win_width or x1<0 or y1>win_height or y1<0:
           gameclose=True
        
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window,yellow,[foodx,foody,snake,snake])
        snake_size=[]
        snake_size.append(x1)
        snake_size.append(y1)
        snake_length_list.append(snake_size)
        if len(snake_length_list)>snake_length:
            del snake_length_list[0]
        game_snake(snake,snake_length_list)
        user_score(snake_length -1)

        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx=round(random.randrange(0,win_width - snake)/10.0)*10.0
            foody=round(random.randrange(0,win_height - snake)/10.0)*10.0
            snake_length +=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

game_loop()