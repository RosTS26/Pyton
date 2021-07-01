print('Самый большой палиндром из умножения 3-хзначных чисел')

a, b = 1000, 1000
t = True

for n in reversed(range(a)):
	print(n)
	for m in reversed(range(b)):
		print(m)
		c = n * m
		c = str(c)
		p = c[::-1]
		if p == c:
			t = False
			break

	if t == False:
		break

print(c, '-- это число палиндром!')		
