input = '3113322113'

def convert_string(input):
	string_divided = []
	previous = ''
	current = ''

	for i in input:
		if previous == '':
			previous = i
		elif i == previous:
			if current == '':
				current = previous + i
			else:
				current = current + i
		else:
			if current != '':
				string_divided.append(current)
				current = ''
				previous = i
			else:
				string_divided.append(previous)
				previous = i
	if current != '':
		string_divided.append(current)
	else:
		string_divided.append(previous)
	# print string_divided

	new_list = []
	for e in string_divided:
		new_list.append(str(len(e)))
		new_list.append(e[0])

	new_string = ''.join(new_list)
	# print new_string
	return new_string

# print convert_string(input)

def iterate(input, n):
	new_input = input
	for i in range(n):
		a = convert_string(new_input)
		new_input = a
		i += 1
	return len(new_input)

print iterate(input, 40)
print iterate(input, 50)



