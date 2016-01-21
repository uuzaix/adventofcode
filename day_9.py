import itertools

with open('day_9.input') as file:
	input = file.readlines()

instructions = dict()
places = []
for line in input:
	splited_line = line.split(' ')
	instructions[(splited_line[0], splited_line[2])] = int(splited_line[4])
	instructions[(splited_line[2], splited_line[0])] = int(splited_line[4])
	places.append(splited_line[0])
	places.append(splited_line[2])

places = set(places)
orderings = itertools.permutations(places)


def distance(orderings):
	result = []
	for e in orderings:
		result.append(instructions[(e[0], e[1])]+instructions[(e[1], e[2])]+instructions[(e[2], e[3])]+instructions[(e[3], e[4])]+instructions[(e[4], e[5])]
			+instructions[(e[5], e[6])]+instructions[(e[6], e[7])])
	return min(result), max(result)

print distance(orderings)


