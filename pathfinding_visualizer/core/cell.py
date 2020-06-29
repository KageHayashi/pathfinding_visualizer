from color import Color
import pygame

class Cell():
    def __init__(self, x, y, cols, rows, grid):
        self.x = x 
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        #values: 1 = current_cell, 2 = open/offspring, 3 = finish, 4 = wall
        self.value = 0
        self.parent = None
        self.wall = False
        self.offsprings = []
        self.cols = cols
        self.rows = rows
        self.grid = grid
        self.gridBase = grid.gridBase
        self.color = None
        self.fill = 1
        self.screen = grid.screen

    def getOffsprings(self):
        x = self.x
        y = self.y
        rows = self.rows
        cols = self.cols
        grid = self.grid
        gridBase = self.gridBase
        #north, south , east, west offsprings
        nsew = ((x, y-1), (x, y+1), (x+1, y), (x-1, y))
        for direction in nsew:
            if direction[0] == -1 or direction[1] == -1:
                continue
            elif direction[0] < cols and direction[0] >= 0 and direction[1] < rows and direction[1] >= 0 and not gridBase[direction[0]][direction[1]].wall:
                self.offsprings.append(gridBase[direction[0]][direction[1]])

        #north-east, south-east, south-west, north-west offsprings
        neseswnw = ((x+1, y-1), (x+1, y+1), (x-1, y+1), (x-1, y-1))
        for direction in neseswnw:
            if direction[0] == -1 or direction[1] == -1:
                continue
            elif direction[0] < cols and direction[0] >= 0 and direction[1] < rows and direction[1] >= 0 and not gridBase[direction[0]][direction[1]].wall:
                self.offsprings.append(gridBase[direction[0]][direction[1]])

    def getColor(self):
        if self.value == 0:
            return Color.BLACK
        elif self.value == 1:
            self.fill = 0
            return Color.BLUE
        elif self.value == 2:
            self.fill = 0
            return Color.GRAY
        elif self.value == 3:
            self.fill = 0
            return Color.GREEN
        elif self.value == 4:
            self.fill = 0
            return Color.RED

    def display(self, color):
        size = self.grid.size
        pygame.draw.rect(self.screen, color, (self.x * size, self.y * size, size, size), 0)
        pygame.display.update()