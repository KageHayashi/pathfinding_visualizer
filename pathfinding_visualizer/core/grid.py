import pygame
from cell import Cell

class Grid:
    def __init__(self, rows, cols, width, height, screen):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.size = height/rows

        self.gridBase = [[None for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.gridBase[i][j] = Cell(i, j, cols, rows, self)

    def display(self):
        size = self.size
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(self.screen, 0, (j * size, i * size, size, size), 1)
        pygame.display.update()

    def showBaseGrid(self):
        rows = self.rows
        cols = self.cols
        gridBase = self.gridBase
        for i in range(rows):
            for j in range(cols):
                if j < cols - 1:
                    print(gridBase[i][j].value, end='  ')
                else:
                    print(gridBase[i][j].value)
    
    def reset(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.gridBase[i][j].fill = 1
                self.gridBase[i][j].g = 0
                self.gridBase[i][j].h = 0
                self.gridBase[i][j].f = 0
                self.gridBase[i][j].offsprings = []
                self.gridBase[i][j].color = None
                self.gridBase[i][j].wall = False
                self.gridBase[i][j].display((255,255,255))
