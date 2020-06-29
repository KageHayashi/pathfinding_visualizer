from cell import Cell
import heuristics
from grid import Grid
from color import Color

def aStar(grid, start, finish):
    openList = []
    closedList = []
    openList.append(start)
    steps = 0
    lowestF = 0
    while len(openList) > 0:
        current_cell = openList[lowestF]
        steps+=1
        for i in range(len(openList)):
            if openList[i].f < current_cell.f:
                current_cell = openList[i]
                lowestF = i

        current_cell.value = 1
        current_cell.f = 0

        openList.pop(lowestF)
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

            #If offspring not in closedList and not blocked then calculate temporary values of g, h, and f.
            if offspring not in closedList:
                tempG = current_cell.g + 1
                tempH = heuristics.calculate_euclidean_heuristics(offspring, finish)
                tempF = tempG + tempH

                #if cell with the same position as offspring is already in the openList with a smaller f value, skip it
                #in other words, put the offspring into the openList if it's not already on the openList or if the cell already in the list has a bigger f value
                if offspring not in openList:
                    offspring.g = tempG
                    offspring.h = tempH
                    offspring.f = tempF
                    openList.append(offspring)
                elif offspring in openList and tempF < offspring.f:
                    offspring.f = tempF
        #end of offspring loop

        #push current_cell onto closedList
        closedList.append(current_cell)

        for child in offsprings:
            child.value = 2
            child.value = 2
            # print(child.x, child.y)
            # print(child.x, child.y, child.f)

        '''FOLOWING USED FOR DEBUGGING'''
        # print("open: ")
        # for cell in openList:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("closed: ")
        # for cell in closedList:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("offsprings: ")
        # for cell in offsprings:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("")

        #Visualize the path
        for i in range(len(openList)):
            openList[i].display(Color.GREEN)

        for i in range(len(closedList)):
            if closedList[i] != start:
                closedList[i].display(Color.RED)

    return False