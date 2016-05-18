import itertools

containers = map(int, open('day_17.input').read().strip().split('\n'))

comb_dict = {}
for i in range(1, len(containers)):
	for combination in itertools.combinations(containers, i):
		if sum(combination) == 150:
			comb_dict[i] = comb_dict.get(i, 0) + 1

print "Total number of combinations: " , sum(comb_dict.values())

min_length = min(comb_dict.keys())
print "Number of combinations for min number of containers: ", comb_dict[min_length]