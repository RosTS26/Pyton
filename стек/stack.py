def greet2(name):
	print(name, 'как твои дела?')

def bye(name):
	print('До свтречи,', name)

def greet1(name):
	print('Привет,', name)
	greet2(name)
	print('Я готов с тобой попрощаться!')
	bye(name)
	print('Конец функции greet1')

name = input('Как тебя зовут? --> ')
greet1(name)