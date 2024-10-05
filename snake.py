import pygame
import sys
import time
import random

pygame.init()

difficulty = 10  #How many movement ticks happen each second min = 1; max = 60
tile_size = 40  #Size of tiles in pixels, should be a divisor of 640
growth = 2      #ammount of extra segments at start
border_mode = 1 #0 - looping; 1 - game over
random.seed(999)

#check difficulty within bounds
if difficulty > 60:
    difficulty = 60
elif difficulty < 1:
    difficulty = 1

#check tile size within bounds
while 640 % tile_size != 0:
    tile_size -=1

#directions
DIR_UP = (0, -tile_size)
DIR_DOWN = (0, tile_size)
DIR_LEFT = (-tile_size, 0)
DIR_RIGHT = (tile_size, 0)

screen = pygame.display.set_mode((640, 640))
tile_count = int(640 / tile_size)
game_tick = int(60/difficulty)
frame = 0
snake_head = pygame.Rect(320, 320, tile_size, tile_size)
segments = [snake_head]
food = pygame.Rect(-640, -640, tile_size, tile_size)
food_spawned = False
score = 0
clock = pygame.time.Clock()
nextmove = DIR_DOWN
currmove = DIR_DOWN

###
def game_over():
    print("Final score: ", score)
    pygame.quit()
    sys.exit()
###

###
def spawn_food():
    global food_spawned
    while not food_spawned:
        x = (random.randint(0, tile_count - 1) * tile_size)
        y = (random.randint(0, tile_count - 1) * tile_size)
        food_spawned = True
        for segment in segments:
            if segment.x == x and segment.y == y:
                food_spawned = False
        food.x = x
        food.y = y
###

###
def draw_food():
    pygame.draw.rect(screen, (255,0,0), food, 0)
###
    
###   
def check_collision():
    global food_spawned, growth, score
    for i in range(1, len(segments)):
        if (segments[i].x == snake_head.x) and (segments[i].y == snake_head.y):
            game_over()
    if border_mode == 1:
        if snake_head.x < 0:
            game_over()
        elif snake_head.x >= 640:
            game_over()
        if snake_head.y < 0:
            game_over()
        elif snake_head.y >= 640:
            game_over()
    if snake_head.x == food.x and snake_head.y == food.y:
        food_spawned = False
        score += len(segments) * difficulty
        growth += 1
###

###            
def move_head():
    global growth, currmove
    #GROWTH CHECK
    if growth > 0:
        growth -= 1
        segments.append(pygame.Rect(segments[-1].x, segments[-1].y, tile_size, tile_size))

    currmove = nextmove
    move_segments()
    snake_head.move_ip(nextmove[0], nextmove[1])
    #OOB CHECKS
    if border_mode == 0:
        if snake_head.x < 0:
            snake_head.move_ip(640, 0)
        elif snake_head.x >= 640:
            snake_head.move_ip(-640, 0)
        if snake_head.y < 0:
            snake_head.move_ip(0, 640)
        elif snake_head.y >= 640:
            snake_head.move_ip(0, -640)
    check_collision()
###

###   
def draw_segments():
    for segment in segments:
        pygame.draw.rect(screen, (255, 255, 255), segment, 0)
###

###        
def move_segments():
    for i in range(len(segments)-1, 0, -1):
        segments[i].x = segments[i-1].x
        segments[i].y = segments[i-1].y
###
        
while True:
    frame += 1 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and currmove != DIR_RIGHT:
                nextmove = DIR_LEFT
            elif event.key == pygame.K_RIGHT and currmove != DIR_LEFT:
                nextmove = DIR_RIGHT
            elif event.key == pygame.K_UP and currmove != DIR_DOWN:
                nextmove = DIR_UP
            elif event.key == pygame.K_DOWN and currmove != DIR_UP:
                nextmove = DIR_DOWN
            #elif event.key == pygame.K_SPACE:
            #    growth +=1
    if frame % game_tick == 0:
        move_head()
        if growth == 0:
            spawn_food()
    screen.fill((0,0,0))
    draw_food()
    draw_segments()    
    pygame.display.update()
    
