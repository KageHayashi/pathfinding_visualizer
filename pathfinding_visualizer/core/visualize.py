import pygame
from grid import Grid
from astar import aStar
from color import Color

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
finished = False
rows, cols = 25, 25
width, height = 500, 500
size = width/cols
grid = Grid(rows, cols, width, height, screen)
gridBase = grid.gridBase


def placeWall(pos, start, finish):
    x = pos[0]
    y = pos[1]
    g1 = x // (width // cols)
    g2 = y // (height // rows)
    wall = gridBase[g1][g2]
    if wall != start and wall != finish:
        wall.wall = True
        wall.display(0)

def selectStart(pos):
    x = pos[0]
    y = pos[1]
    g1 = x // (width // cols)
    g2 = y // (height // rows)
    start = gridBase[g1][g2]
    return start

def selectEnd(pos):
    x = pos[0]
    y = pos[1]
    g1 = x // (width // cols)
    g2 = y // (height // rows)
    finish = gridBase[g1][g2]
    return finish

start, finish = None, None


grid.display()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.init()
            pygame.quit()
            finished = True
            break
        if event.type == pygame.KEYDOWN:
            pos = pygame.mouse.get_pos()
            if event.key == pygame.K_a:
                if start == None:
                    start = selectStart(pos)
                    start.value = 1
                    start.display(Color.BLUE)
            if event.key == pygame.K_s:
                finish = selectEnd(pos)
                finish.value = 3
                finish.display(Color.PURPLE)
            if event.key == pygame.K_q:
                start, end = None, None
                grid.reset()
                grid.display()
                
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                placeWall(pos, start, finish)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                try:
                    aStar(gridBase, start, finish)
                except:
                    pass



        