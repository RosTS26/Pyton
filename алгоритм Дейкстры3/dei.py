def lower_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

processed = []
graph = {}
graph['start'] = {}
graph['start']['a'] = 2
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['c'] = 2
graph['a']['fin'] = 2
graph['b'] = {}
graph['b']['a'] = 2
graph['c'] = {}
graph['c']['b'] = -1
graph['c']['fin'] = 2
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 2
costs['b'] = 2
costs['c'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['fin'] = None

node = lower_cost_node(costs)

while node != None:
	cost = costs[node]
	heighbors = graph[node]

	for n in heighbors.keys():
		new_cost = cost + heighbors[n]

		if new_cost < costs[n]:
			costs[n] = new_cost
			parents[n] = node

	processed.append(node)
	node = lower_cost_node(costs)

print(parents)