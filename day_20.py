def find_dividers(max):
	x = 1
	dividers = []
	while x ** 2 <= max:
		if max % x == 0:
			dividers.append(x)
			dividers.append(max / x)
		x += 1
	return dividers

def find_house(max):
	for house in xrange(10, 10000000, 10):
		gifts = sum(find_dividers(house))
		print (house, gifts)
		if gifts*10 >= max:
			return house
			break


print find_house(34000000)