import itertools

containers = map(int, open('day_17.input').read().strip().split('\n'))

total = 0

min_number_of_cont = len(containers)
comb_dict = {}
for i in range(1, len(containers)):
	comb_dict[i] = 0
	for combination in itertools.combinations(containers, i):
		if sum(combination) == 150:
			total += 1
			comb_dict[i] = comb_dict[i] + 1

print "Total numbwr of combinations: " , total

for n, n_of_comb in comb_dict.iteritems():
	if n == min(n for n, n_of_comb in comb_dict.iteritems() if n_of_comb > 0):
		print "Number of combinations for min number of containers: " , n_of_comb

