import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return  (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2 [0] and (c1[1] == c2[1]))

UP = 0 
RIGHT = 1
DOWN = 2
LEFT = 3 

pygame.init()
canvas = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

#personalizaçao do personagem
snake = [(200, 200), (200, 200),(200, 200)]

snake_skin = pygame.Surface((10,10))
snake_skin.fill((38,129,237))
direction = LEFT
clock = pygame.time.Clock()
#food para alimento
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

#atualizaçao 
while True:
    clock.tick(20)
#criaçao da logica de movimento
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_DOWN:
                direction = DOWN
            if event.key == K_RIGHT:
                direction = RIGHT
            if event.key == K_LEFT:
                direction  = LEFT
            
#logica de moviemento
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    canvas.fill((0,0,0))
    canvas.blit(apple,apple_pos)
    for pos in snake:
        canvas.blit(snake_skin,pos)

            
    pygame.display.update()