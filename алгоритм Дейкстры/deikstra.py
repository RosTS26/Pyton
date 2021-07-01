def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in  processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

# Создаем графы с помощью таблицы
graph = {}

# Хеш-таблица весов всех ребер
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
# print(graph['start']['a'])
# print(graph['start'].keys())
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# Таблица стоимостей узлов (В будущем она будут менять значения)
infinity = float('inf') # Бесконечность
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Хеш-таблица для родителей (В будущем будет менять значение)
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Масив для ослеживания проверенных узлов, чтоб небыло циклов
processed = []

node = find_lowest_cost_node(costs) # Находим узел с наименьшей стоимостью среди необработанных
while node != None: # Если обработаны все узлы, цикл завершается
	cost = costs[node] # Цена равна цене узла, которого мы взяли
	neighbors = graph[node] # Находим соседей для данного узла
	for n in neighbors.keys(): # Перебераем всех соседей по порядку
		new_cost = cost + neighbors[n] # Новая цена равна цене <выбранного узла> + <Цене соседа>
		if costs[n] > new_cost: # Если к соседу можно добраться быстрее
			costs[n] = new_cost # Обновляем стоимость этого узла
			parents[n] = node # Этот узел становится новым родителем для соседа
	processed.append(node) # Заносим узел в список "обработанных"
	node = find_lowest_cost_node(costs) # Находим новый узел и проходим цикл заново



