import pygame
pygame.init

##  ---------COLORS----------  ##
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
##  ---------COLORS----------  ##
screen_size = (800,600)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#--------COORDS AND P1 SPEED--------#
p1_x_coor = 50
p1_y_coor = 300 - 45
p1_y_speed = 0
#--------COORDS AND P1 SPEED--------#


#--------COORDS AND P2 SPEED--------#
p2_x_coor = 750 - player_width
p2_y_coor = 300 - 45
p2_y_speed = 0
#--------COORDS AND P2 SPEED--------#


#-------- COORDS AND BALL SPEED --------#
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3
#-------- COORDS AND BALL SPEED --------#


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #---- LOGIC ----#
        if event.type == pygame.KEYDOWN:
            #J1
            if event.key == pygame.K_w:
                p1_y_speed = -3
            if event.key == pygame.K_s:
                p1_y_speed = 3
            #J2
            if event.key == pygame.K_UP:
                p2_y_speed = -3
            if event.key == pygame.K_DOWN:
                p2_y_speed = 3

        if event.type == pygame.KEYUP:
            #J1
            if event.key == pygame.K_w:
                p1_y_speed = -0
            if event.key == pygame.K_s:
                p1_y_speed = 0
            #J2
            if event.key == pygame.K_UP:
                p2_y_speed = -0
            if event.key == pygame.K_DOWN:
                p2_y_speed = 0
        #---- LOGIC ----#

    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1
    
    #revisa si la pelota sale de la derecha
    if ball_x > 800:
        ball_x = 400
        ball_y = 300
        #si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1

    #revisa si la pelota sale de la izquierdo
    if ball_x < 0:
        ball_x = 400
        ball_y = 300
        #si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1


    #--- MOD COORDS FOR MOVE PLAYERS/BALL ---# 
    p1_y_coor += p1_y_speed
    p2_y_coor += p2_y_speed
    #--- MOD COORDS FOR MOVE PLAYERS/BALL ---# 

    #--- MOD COORDS FOR MOVE PLAYERS/BALL ---# 
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #--- MOD COORDS FOR MOVE PLAYERS/BALL ---# 


    screen.fill(BLACK)
    
    ### ------------ DRAW ZONE---------------------------
    p1= pygame.draw.rect(screen, BLUE, (p1_x_coor, p1_y_coor, player_width, player_height))
    p2= pygame.draw.rect(screen, RED, (p2_x_coor, p2_y_coor, player_width, player_height))
    ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)
    ### ------------ DRAW ZONE---------------------------

    ## ------------- COLLISION ------------------
    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_speed_x *= -1
    ## ------------- COLLISION ------------------

    pygame.display.flip()
    clock.tick(80)
pygame.quit()