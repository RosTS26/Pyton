a = 25
b = 0
c = 0

while True:
	c += 1
	print(a, b, c)
	if a < b < c:
		if a ** 2 + b ** 2 == c ** 2:
			if a + b + c == 1000:
				print('a = ', a)
				print('b = ', b)
				print('c = ', c)
				break

	if c == 500:
		c = 0
		b += 1
		if b == 500:
			b = 0
			a += 1
