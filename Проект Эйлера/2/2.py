print('Сумма четных чисел числа Фибаначи до 4 млн')


c, a, n = 0, 0, 0
b = 1

while b < 4000000:
	c = a + b
	if c % 2 == 0:
		n += c
	print(c)
	a = c + b
	if a % 2 == 0:
		n += a
	print(a)
	b = c + a
	if b % 2 == 0:
		n += b
	print(b)

print('Сумма четных чисел числа Фибаначи меньше 4 млн:', n)