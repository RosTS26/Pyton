# Работает только тогда, когда список отсортирован!
def binary_seartch(list_, item):
	global mid
	low = 0 # Первое значение в списке
	high = len(list_) - 1 #Последнее значение в списке
	while low <= high: # запускаем цикл с условием, что меньшее значение не должно привышать максимальное
		mid = (low + high) // 2 # Находим середнину списка (Если список нечетный, округляем в меньшую сторону)
		guess = list_[mid] # guess принимает значение середины списка
		
		# Сравниваем число с искомым значением, по результату отсеивам одну из частей списка
		if guess == item:
			return mid
		elif item > guess:
			low = mid + 1
		else:
			high = mid - 1
		print(mid)
	return None

def stupid_seartch(list_, item):
	for n in range(0, len(list_) - 1):
		guess = list_[n]
		if guess == item:
			return print(n)

	return None 

my_list = [1, 5, 10, 100, 200, 555, 1000, 2000, 3000, 4000]
binary_seartch(my_list, 555)
print('Из всего списка это то самое число -->',mid,'(', my_list[mid], ')')

stupid_seartch(my_list, 3000)
print(min(my_list))


