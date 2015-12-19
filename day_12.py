import re
import json

with open('day_12.input') as f:
	input = f.read()

# all_numbers = []
all_numbers = (re.findall("-?[0-9]+", input))
# print all_numbers

sum = 0
for i in all_numbers:
	sum = sum + int(i)
print sum