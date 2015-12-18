import re

unknown_sue = {'children': '3', 'cats': '7', 'samoyeds': '2', 'pomeranians': '3', 'akitas': '0', 'vizslas': '0', 'goldfish': '5', 'trees': '3', 'cars': '2', 'perfumes': '1'}

def convert_input(input):
	with open('day_16.input') as f:
		input = f.readlines()

	aunts = {}
	for line in input:
		name = re.findall('(^.*?):', line)
		things = re.findall('^.*?:(.*)', line)[0].replace(' ','').split(',')

		aunts[name[0]] = {x.split(':')[0]:x.split(':')[1] for x in things}
	return aunts


def find_aunt(aunts):
	incorrect_aunts =[]
	for aunt, param in aunts.iteritems(): 
		for key in unknown_sue.keys():
			if key in param.keys() and param[key] != unknown_sue[key]:
				incorrect_aunts.append(aunt)

	for aunt in set(incorrect_aunts):
		del aunts[aunt]
	return aunts

print find_aunt(convert_input(input))