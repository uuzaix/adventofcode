with open('day_2.input') as f:
    input = f.readlines()

def adjust_input(input):
	newcoll = []
	for i in input:
		box = i.split("x")
		newbox = []
		for j in box:
			one = int(j)
			newbox.append(one)
		newbox.sort()
		newcoll.append(newbox)
	return newcoll

def paper(boxes):
	areas = [a*b+2*(a*b + a*c + c*b) for (a, b, c) in boxes]
	return sum(areas)

def ribbon(boxes):
	lengths = [2*(a+b) +a*b*c for (a,b,c) in boxes]
	return sum(lengths)

print paper(adjust_input(input))
print ribbon(adjust_input(input))



