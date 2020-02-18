import pygame
pygame.init()

import random

width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('First pygame game')
running = True
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
YELLOW=(0,255,0)
BLACK=(0,0,0)
screen.fill(WHITE)

#global collisions
collisions = 0 # number of player/ enemy collions detected

xpos = 50
ypos = 50
expos = 1100
eypos = 600

health = 100

paused = False

playerspeed,enemyspeed = 1,0.5 #speeds
player_widthandhight,enemy_widthandhight = 50,50

# create a font for rendering text to screen; need pygame.font.init() if 'pygame.init()' not used
font1 = pygame.font.Font('freesansbold.ttf', 18)
health_textX, health_textY = 50,20 # where to print health value on screen
collision_textX, collision_textY = 900,20 # where to print collions value on screen

def render_text(x,y,text):
    # print(type(data))
    # data = int(data) # make sure that data is an interger so that the decimal places are not printed if a float value
    data_render_obj = font1.render(text, True, WHITE)
    screen.blit(data_render_obj, (x,y))


def draw_entity(x,y,colour,entity_width):
    pygame.draw.rect(screen,colour,(x,y,entity_width,entity_width))
    
def draw_health(ph):
    pygame.draw.rect(screen,BLACK,(50,12.5,100 * 11,30))
    pygame.draw.rect(screen,RED,(50,12.5,ph * 11,30))

def move_enemy(x,y):
    if x > y:
        x = x - enemyspeed
    elif x < y:
        x = x + enemyspeed
    return x

def ymove_enemy(a,b):
    if a > b:
        a = a - enemyspeed
    elif a < b:
        a = a + enemyspeed
    return a

def collision(px,ex,py,ey,p_wh,h,colls):   # collision(xpos,expos,ypos,eypos, player_widthandhight,collisions)
    if px >= ex and px <= ex + p_wh and py >= ey and py <= ey + p_wh: #top left
        draw_entity(ex,ey,WHITE,p_wh) #deleting previous sprite of enemy on death
        draw_entity(px,py,WHITE,p_wh) #deleting previous sprite of player on death
        pygame.draw.rect(screen,BLACK,(0,0,1200,700),99) #border
        pygame.draw.line(screen, WHITE, (px,py), (ex,ey))
        colls = colls + 1
        return 50,50,1100,600,100,colls
    
    elif px + 50 >= ex and px + 50 <= ex + p_wh and py >= ey and py <= ey + p_wh: #top right
        draw_entity(ex,ey,WHITE,p_wh) #deleting previous sprite of enemy on death
        draw_entity(px,py,WHITE,p_wh) #deleting previous sprite of player on death
        pygame.draw.rect(screen,BLACK,(0,0,1200,700),99) #border
        pygame.draw.line(screen, WHITE, (px,py), (ex,ey))
        colls = colls + 1
        return 50,50,1100,600,100,colls
    
    elif px >= ex and px <= ex + p_wh and py + 50 >= ey and py + 50 <= ey + p_wh: #bottom left
        draw_entity(ex,ey,WHITE,p_wh) #deleting previous sprite of enemy on death
        draw_entity(px,py,WHITE,p_wh) #deleting previous sprite of player on death
        pygame.draw.rect(screen,BLACK,(0,0,1200,700),99) #border
        pygame.draw.line(screen, WHITE, (px,py), (ex,ey))
        colls = colls + 1
        return 50,50,1100,600,100,colls
        
    elif px + 50 >= ex and px + 50 <= ex + p_wh and py + 50 >= ey and py + 50 <= ey + p_wh: #bottom right
        draw_entity(ex,ey,WHITE,p_wh) #deleting previous sprite of enemy on death
        draw_entity(px,py,WHITE,p_wh) #deleting previous sprite of player on death
        pygame.draw.rect(screen,BLACK,(0,0,1200,700),99) #border
        pygame.draw.line(screen, WHITE, (px +25 ,py +25 ), (ex +25 ,ey +25 ))
        colls = colls + 1
        return 50,50,1100,600,100,colls
    
    elif health <= 0:
        draw_entity(ex,ey,WHITE,p_wh) #deleting previous sprite of enemy on death
        draw_entity(px,py,WHITE,p_wh) #deleting previous sprite of player on death
        pygame.draw.rect(screen,BLACK,(0,0,1200,700),99) #border
        pygame.draw.line(screen, WHITE, (px +25 ,py +25 ), (ex +25 ,ey +25 ))
        return 50,50,1100,600,100,colls
        
    else:
        return px,py,ex,ey,h,colls

pygame.draw.rect(screen,BLACK,(0,0,1200,700),99) # draw black border

# game loop
while running:

    pressed = pygame.key.get_pressed()

    pygame.draw.line(screen, WHITE, (xpos +25 ,ypos +25 ), (expos +25 ,eypos +25 ))
    
    draw_entity(xpos,ypos,WHITE,player_widthandhight) #deleting previous sprite of player
    
    dpress = pressed[pygame.K_d]
    apress = pressed[pygame.K_a]
    wpress = pressed[pygame.K_w]
    spress = pressed[pygame.K_s]
    escpress = pressed[pygame.K_ESCAPE]
    if dpress and xpos < 1100:
        xpos = xpos + playerspeed
    if apress and xpos > 50:
        xpos = xpos - playerspeed
    if spress and ypos < 600:
        ypos = ypos + playerspeed
    if wpress and ypos > 50:
        ypos = ypos - playerspeed
    if escpress:
        break 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_entity(xpos,ypos,BLUE,player_widthandhight) #player
    
    draw_entity(expos,eypos,WHITE,enemy_widthandhight) #deleting previous sprite of enemy
    expos = move_enemy(expos,xpos)
    eypos = ymove_enemy(eypos,ypos)
    draw_entity(expos,eypos,RED,enemy_widthandhight) # enemy
    
    pygame.draw.line(screen, YELLOW, (xpos +25 ,ypos +25 ), (expos +25 ,eypos +25 ))
   
    health = health - 0.01
    draw_health(health)
    render_text(health_textX,health_textY,"Health: " + str(int(health))) # print health value to screen
    
    render_text(collision_textX,collision_textY,"Collions: " + str(int(collisions))) # print collisions value to screen
   
    pygame.display.update()
    
    xpos,ypos,expos,eypos,health,collisions = collision(xpos,expos,ypos,eypos,player_widthandhight,health, collisions)

            
print('end')


"""

"""