from random import randrange

def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range(p, r):
		if(A[j]<=x):
			i = i+1
			tmp = A[i]
			A[i] = A[j]
			A[j] = tmp
	tmp = A[i+1]
	A[i+1] = A[r]
	A[r] = tmp
	return i+1

def test_partition():
	a = [2, 8, 7, 1, 3, 5, 6, 4]
	q = partition(A=a, p=0, r=len(a)-1)	
	assert(q==3)
	return

def quicksort(A, p, r):
	if(p<r):
		q = partition(A, p, r)
		quicksort(A, p, q-1)
		quicksort(A, q+1, r)
	return

def test_quicksort():
	a = [2, 8, 7, 1, 3, 5, 6, 4]
	quicksort(A=a, p=0, r=len(a)-1)
	assert(a == [1, 2, 3, 4, 5, 6, 7, 8])
	return

def randomized_partition(A, p, r):
	i = randrange(p, r)
	tmp = A[r]
	A[r] = A[i]
	A[i] = tmp
	return partition(A, p, r)

def test_randomized_partition():
	a = [2, 8, 7, 1, 3, 5, 6, 4]
	q = randomized_partition(A=a, p=0, r=len(a)-1)	
	for i in range(q):
		assert(a[i] <= a[q])
	for i in range(q+1, len(a)):
		assert(a[q] <= a[i])
	return

def randomized_quicksort(A, p, r):
	if(p<r):
		q = randomized_partition(A, p, r)
		randomized_quicksort(A, p, q-1)
		randomized_quicksort(A, q+1, r)
	return

def test_randomized_quicksort():
	a = [2, 8, 7, 1, 3, 5, 6, 4]
	randomized_quicksort(A=a, p=0, r=len(a)-1)
	assert(a == [1, 2, 3, 4, 5, 6, 7, 8])
	return

def test():
	test_partition()
	test_randomized_partition()
	test_quicksort()
	test_randomized_quicksort()
	print("Passed all tests\n")
	return

def main():
	test()

	a = [2, 8, 7, 1, 3, 5, 6, 4, 5]
	print("Running Quicksort")
	print("before - a: " + str(a))
	quicksort(A=a, p=0, r=len(a)-1)
	print("after - a : " + str(a))

	a = [2, 8, 7, 1, 3, 5, 6, 4, 5]
	print("")
	print("Running randomized Quicksort")
	print("before - a: " + str(a))
	quicksort(A=a, p=0, r=len(a)-1)
	randomized_quicksort(A=a, p=0, r=len(a)-1)
	print("after - a : " + str(a))
	return

if (__name__ == "__main__"):
	main()