import random

def fastsort(arr):
	if len(arr) < 1:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		great = [i for i in arr[1:] if i > pivot]
		print(pivot)

		return fastsort(less) + [pivot] + fastsort(great)

arr = [random.randrange(1, 100) for i in range(20)]
print(arr)
print(fastsort(arr))