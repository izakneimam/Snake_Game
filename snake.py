import pygame
import random
 
pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake_Game")

relogio = pygame.time.Clock()

comida_x = random.randrange(0,600,20)
comida_y = random.randrange(0,400,20)

x = 100
y = 100
dx = 20
dy = 0
cobra = [(x, y)]

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -20
            elif evento.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = 20
            elif evento.key == pygame.K_LEFT and dx == 0:
                dx = -20
                dy = 0
            elif evento.key == pygame.K_RIGHT and dx == 0:
                dx = 20
                dy = 0

    tela.fill((0, 0, 0))
    
    for parte in cobra:
        pygame.draw.rect(tela, (0, 255, 0), (parte[0], parte[1], 20, 20))
    
    pygame.draw.rect(tela, (255, 0, 0), (comida_x, comida_y, 20, 20))
    
    x += dx
    y += dy


    if x < 0 or x >= 600 or y < 0 or y >= 400:
        rodando = False

    if (x, y) in cobra:
        rodando = False

    cobra.append((x,y))
    
    if x == comida_x and y == comida_y:
        comida_x = random.randrange(0,600,20)
        comida_y = random.randrange(0, 400, 20)
    else:
        cobra.pop(0)

    pygame.display.flip()
    relogio.tick(10)
 

pygame.quit()

