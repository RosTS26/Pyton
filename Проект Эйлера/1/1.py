print('Числа кратные 3 и 5')

n = 0
a = 0
b = 0

for i in range(1000):
	if i % 3 == 0:
		print(i)
		n += i

	elif i % 5 == 0:
		print(i)
		n += i

print('Сумма всех чисел кратных 3 и 5 до 1000 равна:', n)