import re

input = map(str, open('day_8.input').read().strip().split('\n'))

init_length, esc_lenght, unesc_length = 0, 0, 0

for line in input:
	init_length += len(line)
	line = line[1:-1]
	line = re.sub(r'\\x[0-9a-f]{2}', 'A', line)
	line = re.sub(r'\\"', '"', line)
	line = re.sub(r'\\\\', 'B', line)
	esc_lenght += len(line)

for line in input:
    line = re.sub(r'\\', '\\\\\\\\', line)
    line = re.sub(r'"', '\\"', line)
    line = '"' + line + '"'
    unesc_length += len(line)

print (init_length - esc_lenght)
print (unesc_length - init_length)