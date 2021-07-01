from collections import deque

WAY = []
way = {}
way['S'] = ['a', 'b']
way['a'] = ['c', 'F']
way['b'] = ['c', 'd']
way['d'] = ['F']
way['c'] = []
way['start'] = {}
way['start']['a', 'b', 'c', 'd', 'F'] = 1
sortway = deque()
sortway += ['S']

while sortway:
	sw = sortway.popleft()
	if sw == 'F':
		print('самый короткий путь', )
		break
	else:
		sortway += way[sw]

