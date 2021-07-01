def checkvoter(name):
	if voter.get(name):
		print('Ты уже голосовал!')
	else:
		print('Вы еще не голосовали!')
		voter[name] = True

voter = {}
while True:
	name = input('Ваше имя: ')
	checkvoter(name)
