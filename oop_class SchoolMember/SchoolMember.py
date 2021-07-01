import os
import time

class SchoolMember:
	"""docstring for SchoolMember"""
	t = True

	def __init__(self):
		self.name = input('Имя: ')
		self.age = input('Возраст: ')
		name = '\n' + self.name + '				'
		age = self.age + '				'
		f.write(name)
		f.write(age)
	def tell(self):
		'''Вывести информацию'''
		print('Имя: {0} Возраст: {1}'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
	'''Представляет преподавателя'''
	def __init__(self):
		print('\nВведите имя, возраст и зарплату ПРЕПОДОВАТЕЛЯ:')
		print('Чтобы завершить таблицу учителей, введите имя: "-"\n')
		SchoolMember.__init__(self)
		if self.name == '-':
			self.name = '---'
			self.age = '---'
			self.salary = '---'
			SchoolMember.t = False
		if SchoolMember.t == True:
			self.salary = input('Зарплата: ')
			f.write(self.salary)
			print('\n*** Создан Teacher:', self.name, '***')
		else:
			pass
				
	def tell(self):
		SchoolMember.tell(self)
		print('Зарплата:', self.salary)

class Student(SchoolMember):
	'''Представляет студента'''
	def __init__(self):
		print('\nВведите имя, возраст и оценку СТУДЕНТА')
		print('Чтобы завершить таблицу для учеников, введите имя: "-"\n')
		SchoolMember.__init__(self)	
		if self.name == '-':
			self.name = '---'
			self.age = '---'
			self.marks = '---'
			SchoolMember.t = False
		if SchoolMember.t == True:
			self.marks = input('Оценка: ')
			f.write(self.marks)
			print('\n*** Создан Student', self.name, '***')
		else:
			pass

	def tell(self):
		SchoolMember.tell(self)
		print('Оценка:', self.marks)

print('ВНИМАНИЕ! Файл со списком будет создан в корневой папке!')
file = input('Введите имя файла --> ')
if file == '':
	file = 'Member' + time.strftime('%d_%m_%Y') + '.txt'
else:
	file += '.txt'
f = open(file, 'w')
f.write('Имена:					Возраст:			Зарплата/Оценка:')
Teach = []
Stud = []

nt = -1
while SchoolMember.t:
	t = Teacher()
	Teach.append(t)
	nt += 1
	
SchoolMember.t = True
ns = -1
while SchoolMember.t:
	s = Student()
	Stud.append(s)
	ns += 1
	
print()

members_t = Teach[:]
members_s = Stud[:]
for member in members_t:
	member.tell() # Работает как для преподователя, так и для студента

print()

for member in members_s:
	member.tell()

print('\nКол-во учителей =', nt)
print('Кол-во студентов =', ns)

NT = '\n\nКол-во учителей в списке: ' + str(nt) 
NS = '\nКол-во студентов в списке: ' + str(ns) 
f.write(NT)
f.write(NS)
f.close()