def bubble_sort(A):
	for j in range(len(A)):
		for j in range(len(A)-1, 0, -1):
			if(A[j] < A[j-1]):
				tmp = A[j]
				A[j] = A[j-1]
				A[j-1] = tmp
	return

def test_bubble_sort():
	a = [6, 5, 8, 10, 5]
	bubble_sort(A=a)
	assert(a == [5, 5, 6, 8, 10])
	return

def test():
	test_bubble_sort()
	print("All tests passed")

def main():
	test()
	a = [6, 5, 8, 10, 5]
	print("before sort - a: " + str(a))
	bubble_sort(A=a)
	print("after sort - a : " + str(a))
	return

if __name__ == "__main__":
	main()