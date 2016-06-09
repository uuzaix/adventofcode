grid = []
with open('day_18.input') as f:
	for line in f:
		grid.append([int(light) for light in line.replace('#', '1').replace('.', '0').strip()])

def find_neighbors(grid, x, y):
	return sum([grid[i][j] for i in (x+1, x, x-1) for j in (y+1, y, y-1) if (x, y) != (i, j) and len(grid) > i >= 0 and len(grid[x]) > j >= 0])

def change_lights(grid):
	corners = [(0, 0), (0, 99), (99, 0), (99, 99)]
	for corner in corners:
		grid[corner[0]][corner[1]] = 1
	for step in range(100):
		new_grid = [list(n) for n in grid]
		for row in range(100):
			for cell in range(100):
				if (row, cell) not in corners:
					if grid[row][cell] == 1 and find_neighbors(grid, row, cell) != 2 and find_neighbors(grid, row, cell) != 3:
						new_grid[row][cell] = 0
					elif grid[row][cell] == 0 and find_neighbors(grid, row, cell) == 3:
						new_grid[row][cell] = 1
		grid = new_grid
	return grid

print sum(reduce(lambda x, y: x + y, change_lights(grid)))