from collections import deque

def person_is_seller(name):
	return name == 'jonny'

searched = []
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['thom'] = []
graph['peggy'] = []
graph['jonny'] = []
search_queue = deque()
search_queue += graph['you']

while search_queue:
	person = search_queue.popleft()
	if person not in searched:
		if person_is_seller(person):
			print(person, '-- этот человек продает яблоки!')
			break

		else:
			search_queue += graph[person]
			searched.append(person)	
	else:
		print(person, '-- этот человек уже проверялся')