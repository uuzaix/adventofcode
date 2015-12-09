with open('day_6.input') as f:
	input = f.readlines()

grid = [[0 for i in range(1000)] for i in range(1000)]

def fill_in_grid(input):
	for line in input:
		instruction, coord_start, throw, coord_end = line.strip().rsplit(' ', 3)
		coord_start = [int(coord) for coord in coord_start.split(',')]
		coord_end = [int(coord) for coord in coord_end.split(',')]

		for x in range(coord_start[0], coord_end[0]+1):
			for y in range(coord_start[1], coord_end[1]+1):
				if instruction == 'turn on':
					grid[x][y] = 1
				elif instruction == 'turn off':
					grid[x][y] = 0
				else:
					if grid[x][y] == 0:
						grid[x][y] = 1
					else:
						grid[x][y] = 0
	return grid

def count_grid(grid):
	lit = 0
	for row in grid:
		for light in row:
			if light == 1:
				lit += 1
	return lit

print count_grid(fill_in_grid(input))