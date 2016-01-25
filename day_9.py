import itertools

with open('day_9.input') as file:
	input = file.readlines()

instructions = dict()
places = []
for line in input:
	From, _, to, _, distance = line.split(' ')
	instructions[(From, to)] = int(distance)
	instructions[(to, From)] = int(distance)
	places.append(From)
	places.append(to)

places = set(places)
orderings = itertools.permutations(places)


def distance(orderings):
	result = []
	for e in orderings:
		result.append(sum(instructions[(e[i], e[i+1])] for i in range(7)))
	return min(result), max(result)

print distance(orderings)


