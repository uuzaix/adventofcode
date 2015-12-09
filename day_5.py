vowels = 'aeiou'
restricted = ['ab', 'cd', 'pq', 'xy']
# input = ['ugknbfddgicrmopn', 'jchzalrnumimnmhp']
with open('day_5.input') as f:
    input = f.readlines()

def check_vowels(string):
	vowels_counter = 0
	for letter in string:
		if letter in vowels:
			vowels_counter += 1
	return vowels_counter

def check_double(string):
	double_counter = 0
	previous_letter = ''
	for letter in string:
		if letter == previous_letter:
			double_counter += 1
		previous_letter = letter
	return double_counter

def check_restricted(string):
	restricted_counter = 0
	previous_letter = ''
	for letter in string:
		if (previous_letter + letter) in restricted:
			return "naughty"
		previous_letter = letter
	return "nice"

def check_all_criteria(input):
	nice_string = []
	for string in input:
		if check_vowels(string) >= 3:
			if check_double(string) >= 1:
				if check_restricted(string) == 'nice':
					nice_string.append(string)
	return len(nice_string)

print check_all_criteria(input)

# part 2 solution using regexp
import re

def nice_part2(input):
	return len([word for word in input if len(re.findall('(..).*\\1', word)) > 0 and len(re.findall('(.).\\1', word)) > 0])

print nice_part2(input)