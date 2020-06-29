from math import sqrt

def calculate_manhanttan_heuristics(current_cell, finish):
	return abs(current_cell.x - finish.x) + abs(current_cell.y - finish.y)

def calculate_diagonal_heuristics(current_cell, finish):
	return max(abs(current_cell.x - finish.x), abs(current_cell.y - finish.y))

def calculate_euclidean_heuristics(current_cell, finish):
	return sqrt((current_cell.x - finish.x)**2 + (current_cell.y - finish.y)**2)