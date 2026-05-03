import pygame as pygame
import numpy as np
import sys

GREY = (200,200,200)
WHITE = (255,255,255)
BLACK = (0,0,0)

cell_size = 10
cell_number = 80
screen_size = cell_number*cell_size
seed = 0.6


array = np.random.choice([0, 1], size=(cell_number, cell_number), p=[seed, 1-seed])


print(array)


pygame.init()
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SCREEN_UPDATE:
            array_copy = array.copy()

            for a in range(len(array)):
                for b in range(len(array)):
                    count = 0
                    if (a > 0) & (b > 0) and array[a-1, b-1] == 1:
                        count += 1
                    if (a > 0) and array[a-1, b] == 1:
                        count += 1
                    if (a > 0) & (b < cell_number-1) and array[a-1, b+1] == 1:
                        count += 1
                    if (b > 0) and array[a, b-1] == 1:
                        count += 1
                    if (b < cell_number-1) and array[a, b+1] == 1:
                        count += 1
                    if (a < cell_number-1) & (b > 0) and array[a+1, b-1] == 1:
                        count += 1
                    if (a < cell_number-1) and array[a+1, b] == 1:
                        count += 1
                    if (a < cell_number-1) & (b < cell_number-1) and array[a+1, b+1] == 1:
                        count += 1

                    if (array[a, b] == 1) and (count < 2 or count > 3):
                        array_copy[a, b] = 0
                    elif (array[a, b] == 0) and (count == 3):
                        array_copy[a, b] = 1

            array = array_copy.copy()            


    screen.fill(WHITE)

    for x in range(0, screen_size, cell_size):
        pygame.draw.line(screen, GREY, (x,0), (x, screen_size))

    for y in range(0, screen_size, cell_size):
        pygame.draw.line(screen, GREY, (0,y), (screen_size, y))

   ## Draw black squares
    for a in range(0, len(array), 1):
        for b in range(0, len(array), 1):
            if (array[a,b] == 1):
                pygame.draw.rect(screen, BLACK, pygame.Rect(a*cell_size, b*cell_size, cell_size, cell_size))


    #array_copy = array.copy()



    pygame.display.update()
    clock.tick(60)



