bug = 6 # Сумка вместимостью 6 кг
all_list = {} # Полныц список вещей и их вес
must_list = {} # Полный список вещей и их ценность

# Создаем список вещей и их вес
all_list['вода'] = 3
all_list['книга'] = 1
all_list['еда'] = 2
all_list['куртка'] = 2
all_list['камера'] = 1

# Создаем список вещей и их ценность
must_list['вода'] = 10
must_list['книга'] = 3
must_list['еда'] = 9
must_list['куртка'] = 5
must_list['камера'] = 6

must_set = [] # Список в который мы добавим все необходимое

# Создаем двумерный масив (таблицу, в котороую будем вносить данные  вещей)
j = [0 for n in range(bug)]
i = [0 for n in range(len(all_list))]
cell = []
i.append(j)
cell.append(i)
print(cell[1])

# Запускаем цикл по каждой ячейке
for n in all_list:
	for m in range(1, bug + 1):
		thing = all_list[n]
		must = must_list[n]
		if thing == m:
			j[thing] = 1
			 



