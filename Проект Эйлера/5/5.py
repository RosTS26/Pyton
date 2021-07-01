
for n in range(1, 100000000):
	print(n)
	check = 0
	for i in range(1, 21):
		if n % i == 0:
			check += 1
			if check == 20:
				print(n,'--> Самое маленькое число, которое делится с 1 по 20 без остатка')
				break
	if check == 20:
		break
