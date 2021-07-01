import pickle

class idlist():
	"""Данные людей"""
	q = True
	N = 0
	def __init__(self):
		print('\nВведите имя, адрес и номер телефона человека.')
		print('Для завершения списка, введите в поле для ИМЕНИ " - "')

		self.name = input('\nВведите имя: ')
		if self.name == '-':
			idlist.q = False
		else:
			pass

		if idlist.q == True:
			self.adres = input('Введите адрес проживания: ')
			self.numtel = input('Введите номер телефона: ')
			name = '\n' + self.name + '			'
			adres = self.adres + '			'
			numtel = self.numtel
			f1.write(name)
			f1.write(adres)
			f1.write(numtel)
			al[self.name] = self.adres, self.numtel
			idlist.N += 1
			print('\nСоздан профиль *** ' + self.name + ' ***')
			
		else:
			pass

	def tell(self):
		print('Имя: {0}  Адрес: {1}  Номер телефона: {2}'.format(self.name, self.adres, self.numtel))

print('\n!ВНИМАНИЕ!\nАдресная книга будет создана в корневой папке программы!')
f2 = open('adres.data', 'rb')
people = pickle.load(f2)
print('Существующие контакты: ', people)
f2.close()

f1 = open('AdresList.txt', 'w')
f1.write('ИМЕНА:			АДРЕСА:			НОМЕРА ТЕЛЕФОНОВ:')

AL = []
al = {}
while idlist.q:
	i = idlist()
	# i.__init__()
	AL.append(i)
	
print('Всего создано контактов:', idlist.N)

members = AL[:]
for member in members:
	member.tell()

Num = '\n\nКоличество созданых контактов: ' + str(idlist.N)
f1.write(Num)
f1.close()

f2 = open('adres.data', 'wb')
pickle.dump(al, f2)
f2.close()