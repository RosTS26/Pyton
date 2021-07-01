def low_cost_none(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['fin'] = infinity
costs['c'] = infinity
costs['d'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
parents['c'] = None
parents['d'] = None

processed = []

node = low_cost_none(costs)

while node != None:
	cost = costs[node]
	heighbors = graph[node]

	for n in heighbors.keys():
		new_cost = cost + heighbors[n]

		if new_cost < costs[n]:
			costs[n] = new_cost
			parents[n] = node

	processed.append(node)
	node = low_cost_none(costs)

print(parents)