from itertools import combinations
from operator import mul

presents = map(int, open('day_24.input').read().strip().split('\n'))

def split_presents(presents, groups):
	weight = sum(presents)/groups

	for i in range(1, len(presents)):
		good = [c for c in combinations(presents, i) if sum(c) == weight]
		if len(good) > 0:
			break
	return min([reduce(mul, x) for x in good])

print split_presents(presents, 3)
print split_presents(presents, 4)