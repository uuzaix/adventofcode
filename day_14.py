import itertools

input = map(str, open('day_14.input').read().strip().split('\n'))

total_time = 2503
conditions = {}
for condition in input:
	name, _, _, speed, _, _,time, _, _, _, _, _, _, rest_time, _ = condition.split(' ')
	conditions[name] = [int(speed), int(time), int(rest_time)]

def find_distance(total_time):
	result = {}
	for name, (speed, time, rest_time) in conditions.iteritems():
		quotient = total_time // (time + rest_time)
		remainder = total_time % (time + rest_time)
		if remainder >= time:
			result[name] = speed*(quotient+1)*time
		else:
			result[name] = speed*quotient*time + remainder*speed
	max_dist = max(result.values())
	return [(k,val) for k, val in result.items() if val == max_dist]

print find_distance(total_time)[0][1]


def find_score(total_time):
	scores = {}
	for t in range(1, total_time + 1):
		for name, _ in find_distance(t):
			scores[name] = scores.get(name, 0) + 1
	return max(scores.values())

print find_score(total_time)


