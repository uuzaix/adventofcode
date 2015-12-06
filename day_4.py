import md5
input = "bgvyzdsv"
def hashes(input):
	for i in range(1000000):
		key_input = input + str(i)
		if md5.new(key_input).hexdigest()[:6] == "000000":
			return i
print hashes(input)
