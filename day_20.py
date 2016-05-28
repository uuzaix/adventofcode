def find_dividers(max):
	x = 1
	dividers = set()
	while x ** 2 <= max:
		if max % x == 0:
			dividers.add(x)
			dividers.add(max / x)
		x += 1
	return dividers

def find_house(max):
	part_1, part_2 = None, None
	for house in xrange(10, 10000000, 10):
		dividors = find_dividers(house)
		if not part_1:
			gifts1 = sum(dividors)
			if gifts1*10 >= max:
				part_1 = house
		if not part_2:
			gifts2 = sum(d for d in dividors if house/d <= 50)
			if gifts2*11 >= max:
				part_2 = house
				break
	return part_1, part_2

print find_house(34000000)