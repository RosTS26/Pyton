arr = []
n = 10000

for i in range(2, n + 1):
	for j in range(2, i):
		if i % j == 0:
			break

	else:
		arr.append(i)
		print(i)

print('ЭТО 1001 простое число!', arr[1001])			



