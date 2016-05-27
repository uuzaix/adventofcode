import re

with open('day_12.input') as f:
	input = f.read()

def find_numbers(input):
	return sum(map(int, re.findall("-?[0-9]+", input)))

print find_numbers(input)