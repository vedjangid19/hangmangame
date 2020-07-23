import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((900,520))
pygame.display.set_caption("Hangman Game")
img1 = pygame.image.load('images/hm1.png')


black =(10,10,10)
white =(255,255,255)
blue = (90,90,200)
green = (95,200,90)

screen.fill((60,25,60))
screen.blit(img1, [0,0]) 

#######random world

def random_world_generate():
    global random_word
    with open("hangman word.txt","r") as f:
        words = f.read()
    list_of_word = words.split("\n")
    random_word = random.randint(0,len(list_of_word))
    random_word = list_of_word[random_word].lower()

    print("cumputer gess word : ",random_word)
   
##################

######play_music#######

def play_sound():
    song_list = ['Chill.mp3','ChillClear.mp3','Fever.mp3']
    file=random.randint(0,2)
    file = song_list[file]
    file = "sounds/"+file
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
def stop_sound():
    pygame.mixer.music.stop()

####################


def draw_circle(screen,black,circle_x,circle_y):
    pygame.draw.circle(screen,black,(circle_x,circle_y),32)

font = pygame.font.SysFont(None,68)
def text_score(score,color,x,y):
    screen_text = font.render(score,True,color)
    screen.blit(screen_text,[x,y])

list = ['A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z'
        ]
def print1(m0,m1):
    
    x,y =10,375
    list_x =[]
    list_y =[375,450]        
    circle_x = 35
    circle_y = 398
    i=0
    for lat in list:
        i+=1

        if x < m0 < x+65 and y < m1 < y+54:
            draw_circle(screen,(20,20,20),circle_x,circle_y)
            text_score(lat,blue,x+15,y)
        else:
            draw_circle(screen,(50,50,50),circle_x,circle_y)
            text_score(lat,blue,x+15,y)
            
        list_x.append(x)
        x+=70
        circle_x+=70
        

        if i == 13:
            x = 10 
            y = 450
            circle_x= 35
            circle_y = 474



def game_loop():
    random_world_generate()
    exitgame = False
    gameover = False
    clock = pygame.time.Clock()
    fps = 30
    list2 = []
    screen.fill((60,60,60))
    img1 = pygame.image.load('images/hm1.png')
    
    string_x =0
    string_x1 =0
    string_y = 200
    key_down_count = 0
    your_word = []
    for i in range(len(random_word)):
        text_score('_',blue,string_x1+50,string_y)
        string_x1+=51  
    
    circle_x1,circle_y1 = 75 ,120
    text_score("Find Hidden word otherwise you hang !",blue,5,5)
    for i in range(len(random_word)):
        draw_circle(screen,(200,200,0),circle_x1,circle_y1)
        circle_x1+=60
    image_count=1
    wrong = 0
    set_of_random_word = set(random_word)
    as_count=0
    play_sound()
    while not exitgame:

        as_count=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
            
            if event.type == MOUSEBUTTONDOWN:
                mousep = pygame.mouse.get_pos()
                x,y =10,375
                list_x =[]
                list_y =[375,450]        
                
                i=0
                if key_down_count != len(random_word)+3:
                    for lat in list:
                        i+=1
                        if x+10 < mousep[0] < x+60 and y < mousep[1] < y+54:
                            key_down_count+=1
                            if lat.lower() in random_word:
                                your_word.append(lat.lower()) 
                                text_score(lat,blue,string_x+50,string_y)
                                string_x+=50
                            else:
                                wrong +=1
                                image_count+=1
                                if image_count < len(random_word)+2:
                                    name_set_image = "images/hm"+str(image_count)+".png"
                                    img1 = pygame.image.load(name_set_image)
                                if wrong == len(random_word):
                                    img1 = pygame.image.load('images/hm7.png')

                        list_x.append(x)
                        x+=70
                        if i == 13:
                            x = 0 
                            y = 450
        
        for i in set_of_random_word:
            if i in your_word:
                as_count+=1
                if as_count==len(set_of_random_word):
                    screen.fill(black)
                    text_score("Press Space key to play again !",blue,70,10)
                    text_score("you win !",blue,350,240)
                    text_score(f"Hidden word is : {random_word.upper()}",blue,12,100)

                    stop_sound()
                    

        if image_count == 7:
            screen.fill(black)
            text_score("Press Space key to play again !",blue,70,10)
            text_score(f"Hidden word is : {random_word}",blue,12,100)
            text_score("you loss",blue,350,240)
            img1 = pygame.image.load('images/hm7.png')
            stop_sound()
            

        if key_down_count == len(random_word)+3:
            your_string = ""
            for i in random_word:
                if i not in your_word:
                    # print("ok")
                    screen.fill(black)
                    text_score("Press Space key to play again !",blue,70,10)
                    text_score(f"Hidden word is : {random_word}",blue,12,100)
                    text_score("you loss",blue,350,240)
                    img1 = pygame.image.load('images/hm7.png')
                    stop_sound()
                   
                    break

                else:
                    screen.fill(black)
                    
                    text_score("you win",blue,350,240)
                    text_score("Press Space key to play again !",blue,70,10)
                    text_score(f"Hidden word is : {random_word.upper()}",blue,12,100)
                    stop_sound()
                    
            
        mouse = pygame.mouse.get_pos()
        m0,m1 = mouse[0],mouse[1] 
        print1(m0,m1) 
        screen.blit(img1, [680,100])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

game_loop()