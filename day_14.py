import itertools

input = map(str, open('day_14.input').read().strip().split('\n'))

total_time = 2503
conditions = {}
for condition in input:
	name, _, _, speed, _, _,time, _, _, _, _, _, _, rest_time, _ = condition.split(' ')
	conditions[name] = [int(speed), int(time), int(rest_time)]

def find_distance(total_time):
	result = {}
	for key, param in conditions.iteritems()		:
		speed, time, rest_time = param
		name = key
		quotient = total_time // (time + rest_time)
		remainder = total_time % (time + rest_time)
		if remainder >= time:
			result[name] = speed*(quotient+1)*time
		else:
			result[name] = int(speed)*quotient*int(time) + remainder*int(speed)
	max_dist = max(result.values())
	return [{k:val} for k, val in result.items() if val == max_dist]

print find_distance(total_time)[0].values()[0]


def find_score(total_time):
	scores = {}
	for t in range(1, total_time + 1):
		interm_result = find_distance(t)
		for deer in interm_result:
			scores[deer.keys()[0]] = scores.get(deer.keys()[0], 0) + 1
	return max(scores.values())

print find_score(total_time)


