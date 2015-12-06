with open('day_1.input') as f:
    input = f.readline()

def floor(input):
	floor = 0
	for i in input:
		if i == "(":
			floor = floor +1
		else:
			floor = floor - 1
	return floor

def counter(input):
	floor = 0
	count = 0
	for i in input:
		if floor != -1:
			if i == "(":
				floor = floor +1
				count = count +1
			else:
				floor = floor - 1
				count = count + 1
	return count

print floor(input)
print counter(input)