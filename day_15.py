input = [[5,-1, 0, 0, 5], [-1, 3, 0, 0, 1], [0, -1, 4, 0, 6], [-1, 0, 0, 2, 8]]

result = 0
max = 0

for i in range(0,100):
	for j in range(0, 100-i):
		for k in range(0, 100-i-j):
			m = 100 - i - j - k
			cap = input[0][0]*i + input[1][0]*j + input[2][0]*k + input[3][0]*m
			dur = input[0][1]*i + input[1][1]*j + input[2][1]*k + input[3][1]*m
			flav = input[0][2]*i + input[1][2]*j + input[2][2]*k + input[3][2]*m
			tex = input[0][3]*i + input[1][3]*j + input[2][3]*k + input[3][3]*m
			if cap <= 0 or dur <= 0 or flav <= 0 or tex <= 0:
				result = 0
			else:
				result = cap*dur*flav*tex
			if result > max:
				max = result
print max


