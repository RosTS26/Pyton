import pickle

class contactlist():
	"""docstring for contactlist"""
	tr =True
	def __init__(self):
		print('\nВведите имя и номер телефона нового контакта!\n')
		self.name = input('Введите имя: ')
		self.numtel = input('Введите номер телефона: ')
		print('*** Создан контакт', self.name, '***\n')
		cl[self.name] = self.numtel

print('С помощью этой программы вы можете создать и редактировать свой список контактов!\n')

cl = {}
people = 0
file = 'contactlist.data'
file1 = 'people.data'

f = open(file, 'rb')
f1 = open(file1, 'rb')
try:
	cl = pickle.load(f)
	people = pickle.load(f1)
except EOFError:
	pass  
f.close()
f1.close()

info = '''			*** СПИСОК КОМАНД ***
	Для простомтра списка контактов, введите "Просмотр"
	Для добавление контакта в список, введие "Добавить"
	Для удаления контакта из списка, введите "Удалить"
	Чтобы найти контак, введите "Найти"
	Чтобы показать список команд повтоно, введите "help"
	!!! Чтобы сохраните изменения, введите "Сохранить" !!!
'''
print(info)

while True:
	comand = input('Что будем делать?(Впишите команду) --> ').lower()

	if comand == 'просмотр':
		print()
		for key in cl:
			print('Имя:', key, 'Номер телефона:', cl[key])

		print('\nВсего контактов:', people, '\n')

	elif comand == 'найти':
		while True:
			try:
				n = input('\nВведите имя контакта: ')
				if n == 'отмена':
					break

				cl[n]
			except KeyError:
				print('\nТакого контакта не существует!\nПовторите попытку')
				print('Для отмены операции, введите "отмена"\n')
				continue
			print('Имя:', n, 'Номер телефона:', cl[n])
			break

	elif comand == 'удалить':
		while True:
			try:
				d = input('Введите имя контакта, которого хотите удалить: ')
				if d == 'отмена':
					break

				del cl[d]
				people -= 1
			except KeyError:
				print('\nТакого контакта не существует!\nПовторите попытку\n')
				print('Для отмены операции, введите "отмена"\n')
				continue
			print('Контакт "' + d + '" удален!\n')
			break

	elif comand == 'добавить':
		contactlist()
		people += 1

	elif comand == 'help':
		print(info)

	elif comand == 'сохранить':
		print('*** СОХРАНЕНИЕ ***')
		break

	else:
		print('Введене неверная команда!\nПовторите попытку!\n')

f = open(file, 'wb')
f1 = open(file1, 'wb')
pickle.dump(cl, f)
pickle.dump(people, f1)
f.close()
f1.close()
input()
