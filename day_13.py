import itertools

input = map(str, open('day_13.input').read().strip().split('\n'))

relations = {}
persons = set ()
for condition in input:
	From, _, gain, value, _, _, _, _, _, _, to = condition.split(' ')
	if gain == "lose":
		value = int(value)*-1
	else:
		value = int(value)
	persons.add(From)
	relations[(From, to.strip('.'))] = value

orderings = itertools.permutations(persons)

def calculate_happy(orderings):
	max_happy = 0
	for e in orderings:
		happy = 0
		for i in range(len(e)):
			person1 = e[i]
			person2 = e[i-1]
			happy += relations[person1, person2]
			happy += relations[person2, person1]
			if max_happy < happy:
				max_happy = happy
	return max_happy

print calculate_happy (orderings)

for person in persons:
	relations[person, 'me'] = 0
	relations['me', person] = 0
persons.add('me')

orderings_with_me = itertools.permutations(persons)

print calculate_happy (orderings_with_me)


