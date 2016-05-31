import itertools
import re

inputs = map(str, open('day_19.input').read().strip().split('\n'))
molec = inputs[-1]

all_molec = set ()
for line in inputs[:-2]:
	old, _, new = line.split(" ")
	for ind in range(len(molec)):
		if molec[ind:ind+len(old)] == old:
			molec_new = molec[:ind] + new + molec[ind+len(old):]
			all_molec.add(molec_new)

print len(all_molec)
