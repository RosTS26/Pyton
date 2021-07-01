from colorama import Fore, Back, Style
from colorama import init
import time
# from colorama import colored
init() 

print(Fore.RED, Back.GREEN + 'Привет! Это мой первый калькулятор! Не суди строго :) \n Для начала нажми "Enter"')
print(Style.RESET_ALL)
input()

while True:
	print(Fore.BLACK, Back.YELLOW)
	
	while True:
		try:
			a = float(input('Введи любое число: '))
			if type(a) == float:
				break
		except ValueError:
			print('Такого числа несуществует!')
	opr = input('Какое вычисление будем проводить? (Например: +, -, *, /, ^, Корень): ').lower()
	while True:
		try:	
			b = float(input('Введи второе число: '))
			if type(b) == float:
				break
		except ValueError:
			print('Такого числа несуществует!')
	
	print(Style.RESET_ALL)

	def cal(b):	
		while True:
			print(Back.BLUE)	
			if opr == '+':
				c = a + b
				print('Результат вычисления "СЛОЖЕНИЯ" составляет:', c, '\n')
				break
			elif opr == '-':
				c = a - b
				print('Результат вычисления "ВЫЧИТАНИЯ" составляет:', c, '\n')
				break
			elif opr == '*':
				c = a * b
				print('Результат вычисления "УМНОЖЕНИЯ" составляет:', c, '\n')
				break
			elif opr == '/':
				if b == 0:
					print(Style.RESET_ALL)
					while b == 0:
						print(Fore.BLACK, Back.RED + 'Ты чего! На 0 делить нельзя! :(') 
						b = float(input('Запиши другое число: '))
						print(Style.RESET_ALL)		
					c = a / b
					print(Back.BLUE + 'Результат вычисления "ДЕЛЕНИЯ" составляет:', c, '\n')
					break
				else:
					c = a / b
					print('Результат вычисления "ДЕЛЕНИЯ" составляет:', c, '\n')
					break	
			elif opr == '^':
				c = a ** b
				print('Результат вычисления "ВОЗВЕДЕНИЕ В СТЕПЕНЬ" составляет:', c, '\n')
				break
			elif opr == 'корень':
				c = a ** (1/b)
				print('Результат вычисления "КОРНЯ" составляет:', c, '\n')
				break
			elif opr == '%':
				c = a / 100 * b
				print('Результат вычисления "ПРОЦЕНТА" составляет:', c, '\n')
				break
			else:
				print('Выбрано неправильное действие! Повторите попытку.\n')
				break
		print(Style.RESET_ALL)

	cal(b)

