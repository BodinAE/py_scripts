import pygame
import sys
import time

pygame.init()

difficulty = 5
tile_size = 80

if difficulty > 60:
    difficulty = 60
elif difficulty < 1:
    difficulty = 1
screen = pygame.display.set_mode((640, 640))
game_tick = int(60/difficulty)
x_speed = 0
y_speed = 0
frame = 0
snake_head = pygame.Rect(0, 0, tile_size, tile_size)
clock = pygame.time.Clock()

def move_head():
    snake_head.move_ip(x_speed, y_speed)
    if snake_head.x < 0:
        snake_head.move_ip(640, 0)
    if snake_head.x >= 640:
        snake_head.move_ip(-640, 0)
    if snake_head.y < 0:
        snake_head.move_ip(0, 640)
    if snake_head.y >= 640:
        snake_head.move_ip(0, -640)

while True:
    frame += 1 
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -tile_size
                y_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = tile_size
                y_speed = 0
            elif event.key == pygame.K_UP:
                x_speed = 0
                y_speed = -tile_size
            elif event.key == pygame.K_DOWN:
                x_speed = 0
                y_speed = tile_size
    if frame % game_tick == 0:
        move_head()
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), snake_head, 0)
    
    pygame.display.update()
    
