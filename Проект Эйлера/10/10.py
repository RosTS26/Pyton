n = 19999
k = 0

for n in range(2, n + 1):
	for j in range(2, n):
		if n % j == 0:
			break

	else:
		k += n
		print(k)

print('Сумма простых чисел:', k)
