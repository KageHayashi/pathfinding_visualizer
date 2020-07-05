from cell import Cell
import heuristics
from grid import Grid
from color import Color

def aStar(grid, start, finish):
    openCells = []
    closeCells = []
    openCells.append(start)
    steps = 0
    lowestF = 0
    while len(openCells) > 0:
        current_cell = openCells[lowestF]
        steps+=1
        for i in range(len(openCells)):
            if openCells[i].f < current_cell.f:
                current_cell = openCells[i]
                lowestF = i

        current_cell.value = 1
        current_cell.f = 0

        openCells.pop(lowestF)
        current_cell.getOffsprings()
        offsprings = current_cell.offsprings

        #for each offspring
        for offspring in offsprings:
            x = offspring.x
            y = offspring.y
            #if offspring is the goal, stop search
            if x == finish.x and y == finish.y:
                offspring.g = current_cell.g + 1
                offspring.h = heuristics.calculate_euclidean_heuristics(offspring, finish)
                offspring.f = offspring.g + offspring.h
                print("Done")
                print("Steps taken:", steps)
                offspring.value = 3
                return True

            #If offspring not in closeCells and not blocked then calculate temporary values of g, h, and f.
            if offspring not in closeCells:
                tempG = current_cell.g + 1
                tempH = heuristics.calculate_euclidean_heuristics(offspring, finish)
                tempF = tempG + tempH

                #if cell with the same position as offspring is already in the openCells with a smaller f value, skip it
                #in other words, put the offspring into the openCells if it's not already on the openCells or if the cell already in the list has a bigger f value
                if offspring not in openCells:
                    offspring.g = tempG
                    offspring.h = tempH
                    offspring.f = tempF
                    openCells.append(offspring)
                elif offspring in openCells and tempF < offspring.f:
                    offspring.f = tempF
        #end of offspring loop

        #push current_cell onto closeCells
        closeCells.append(current_cell)

        for child in offsprings:
            child.value = 2
            child.value = 2
            # print(child.x, child.y)
            # print(child.x, child.y, child.f)

        '''FOLOWING USED FOR DEBUGGING'''
        # print("open: ")
        # for cell in openCells:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("closed: ")
        # for cell in closeCells:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("offsprings: ")
        # for cell in offsprings:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("")

        #Visualize the path
        for i in range(len(openCells)):
            openCells[i].display(Color.GREEN)

        for i in range(len(closeCells)):
            if closeCells[i] != start:
                closeCells[i].display(Color.RED)

    return False