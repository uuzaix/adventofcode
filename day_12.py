import re
import json

# PART 1
with open('day_12.input') as f:
	input = f.read()


def find_numbers(input):
	return sum(map(int, re.findall("-?[0-9]+", input)))

print find_numbers(input)

# PART 2

with open('day_12.input') as f:
	data = json.load(f)

def sum_without_red(data):
	total = 0
	if isinstance(data, dict):
		if "red" in data.keys() or "red" in data.values():
			return 0
		for item in data.keys():
				total += sum_without_red(data[item])
	elif isinstance(data, list):
		for item in data:
			total += sum_without_red(item)
	elif isinstance(data, int):
		total += data
	return total

print sum_without_red(data)