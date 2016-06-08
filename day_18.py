grid = []
with file('day_18.input', 'r') as f:
	for line in f:
		row = list(line.strip().replace('#', '1').replace('.', '0'))
		new_row = []
		for light in row:
			new_row.append(int(light))
		grid.append(new_row)


def find_neighbors(grid, x, y):
	return sum([int((grid[i][j])) for i in (x-1, x, x+1) for j in (y-1, y, y+1) if (i, j) != (x, y) and len(grid) > i >= 0 and len(grid) > j >= 0])

def change_lights(grid):
	for i in range(100):
		new_grid = [list(row) for row in grid]
		for row in range(len(grid)):
			for cell in range(len(grid[row])):
				if grid[row][cell] == 1 and find_neighbors(grid, row, cell) != 2 and find_neighbors(grid, row, cell) != 3:
					new_grid[row][cell] = 0
				elif grid[row][cell] == 0 and find_neighbors(grid, row, cell) == 3:
					new_grid[row][cell] = 1
				else:
					new_grid[row][cell] = grid[row][cell]
		grid = new_grid
	return grid

print sum(reduce(lambda x, y: x+y, change_lights(grid)))


