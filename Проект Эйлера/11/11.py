import random

def max_4(arr):
	global MAX, route
	m1, m2, m3 = 0, 0, 0
	
	for n in range(4):
		try:
			m1 += arr[i][j + n]
			m2 += arr[i + n][j + n]
			m3 += arr[i + n][j]
		except IndexError:
			return

	if MAX < m1:
		MAX = m1
		# num = [a1, a2, a3, a4]
		route = 'Горизнтольное'

	if MAX < m2:
		MAX = m2
		# num = [a1, c2, c3, c4]
		route = 'По диагонали'

	if MAX < m3:
		MAX = m3
		# num = [a1, b2, b3, b4]
		route = 'Вертикально'

arr = []
for n in range(20):
	i = [random.randrange(1, 100) for i in range(20)]
	arr.append(i)
MAX = 0

while True:
	for i in range(20):
		print(arr[i])
		for j in range(20):
			max_4(arr)	
	break

print('\nМаксимальное множество из 4-х цифр в 3-х направлениях:', MAX)
# print('Список этих цифр:', num)
print('Напрваление:', route)