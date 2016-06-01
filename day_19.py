from random import shuffle

inputs = map(str, open('day_19.input').read().strip().split('\n'))
molec = inputs[-1]
repos = []

all_molec = set ()
for line in inputs[:-2]:
	old, _, new = line.split(" ")
	repos.append((old, new))
	for ind in range(len(molec)):
		if molec[ind:ind+len(old)] == old:
			molec_new = molec[:ind] + new + molec[ind+len(old):]
			all_molec.add(molec_new)

print len(all_molec)

# part2
target = molec
count = 0

while target != 'e':
	tmp = target
	for old, new in repos:
		if new not in target:
			continue
		else:
			target = target.replace(new, old, 1)
			count += 1
	if tmp == target:
		target = molec
		count = 0
		shuffle(repos)

print count
