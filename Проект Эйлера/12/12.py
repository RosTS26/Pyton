divisor = []
n = 0


for i in range(1, 10000000000):
	n += i
	print(len(divisor))
	divisor = []
	
	for j in range(1, n + 1):
		if n % j == 0:
			divisor.append(j)
	
	if len(divisor) > 100:
		break
	# arr.append(divisor)	

print('\nЧисло которое имеет более 100-a делителей:', n)
print(divisor)