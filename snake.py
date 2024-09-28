import pygame
import sys
import time

pygame.init()

difficulty = 5
tile_size = 40
growth = 5

if difficulty > 60:
    difficulty = 60
elif difficulty < 1:
    difficulty = 1
screen = pygame.display.set_mode((640, 640))
game_tick = int(60/difficulty)
x_speed = 0
y_speed = tile_size
frame = 0
snake_head = pygame.Rect(0, 0, tile_size, tile_size)
segments = [snake_head]
clock = pygame.time.Clock()

def check_collision():
    for i in range(1, len(segments)):
        if (segments[i].x == snake_head.x) and (segments[i].y == snake_head.y):
            pygame.quit()
            sys.exit()
            
def move_head():
    global growth
    move_segments()
    snake_head.move_ip(x_speed, y_speed)
    if snake_head.x < 0:
        snake_head.move_ip(640, 0)
    if snake_head.x >= 640:
        snake_head.move_ip(-640, 0)
    if snake_head.y < 0:
        snake_head.move_ip(0, 640)
    if snake_head.y >= 640:
        snake_head.move_ip(0, -640)
    if growth > 0:
        growth -= 1
        #print(len(segments))
        segments.append(pygame.Rect(0, 0, tile_size, tile_size))
    check_collision()

def draw_segments():
    for segment in segments:
        pygame.draw.rect(screen, (255, 255, 255), segment, 0)

def move_segments():
    for i in range(len(segments)-1, 0, -1):
        #print(segments[i].x)
        #print(segments[i].y)
        segments[i].x = segments[i-1].x
        segments[i].y = segments[i-1].y
        
while True:
    frame += 1 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_speed != tile_size:
                x_speed = -tile_size
                y_speed = 0
            elif event.key == pygame.K_RIGHT and x_speed != -tile_size:
                x_speed = tile_size
                y_speed = 0
            elif event.key == pygame.K_UP and y_speed != tile_size:
                x_speed = 0
                y_speed = -tile_size
            elif event.key == pygame.K_DOWN and y_speed != -tile_size:
                x_speed = 0
                y_speed = tile_size
    if frame % game_tick == 0:
        move_head()
    screen.fill((0,0,0))
    draw_segments()
    
    pygame.display.update()
    
