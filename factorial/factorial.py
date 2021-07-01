def factorial(n):
	if n == 0:
		return 1

	else:
		return factorial(n - 1) * n
		

n = int(input('Введите число: '))
# factorial(n)
print('Факториал числа {n} равен {f}!'.format(n = n, f = factorial(n)))

input()

f = 1
for i in range(1, n + 1):
	f = f * i 

print('Факториал числа {n} через цикл равен {f}'.format(n = n, f = f))
