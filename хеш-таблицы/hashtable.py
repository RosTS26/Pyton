arr = {}

for i in range(5):
	key = input('Введите наименование продукта: ')
	arr[key] = float(input('Цена: '))

print(arr)

while True:
	key = input('Продукт: ')
	print('Цена: ', arr.get(key))