with open('day_23.input') as f:
	input = []
	for line in f:
		input.append(line.strip().replace(',', '').split(" "))

register = {'a': 0, 'b': 0}
i = 0

while i < len(input):
	instr = input[i]
	if instr[0] == 'hlf':
		register[instr[1]] /= 2
	elif instr[0] == 'tpl':
		register[instr[1]] *= 3
	elif instr[0] == 'inc':
		register[instr[1]] += 1
	elif instr[0] == 'jmp':
		i += int(instr[1]) - 1
	elif instr[0] == 'jie':
		if register[instr[1]] % 2 == 0:
			i += int(instr[2]) -1
	elif instr[0] == 'jio':
		if register[instr[1]] == 1:
			i += int(instr[2]) -1
	i += 1
print register['b']
