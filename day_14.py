import itertools

input = map(str, open('day_14.input').read().strip().split('\n'))

total_time = 2503
conditions = {}

result = []
for condition in input:
	name, _, _, speed, _, _,time, _, _, _, _, _, _, rest_time, _ = condition.split(' ')
	quotient = total_time // (int(time) +int(rest_time))
	remainder = total_time % (int(time) + int(rest_time))
	if remainder >= int(time):
		result.append(int(speed)*(quotient+1)*int(time))
	else:
		result.append(int(speed)*quotient*int(time) + remainder*int(speed))

print max(result)