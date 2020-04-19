def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]

		i = j-1
		while(i >= 0 and A[i] > key):
			A[i + 1] = A[i]
			i = i-1
		A[i+1] = key

def test_insertion_sort():
	A = [5, 3, 10, 15, 2]
	insertion_sort(A)
	assert(A == [2, 3, 5, 10, 15])

def main():
	test_insertion_sort()

	A = [5, 3, 10, 10, 15, 2]
	print("before: " + str(A))
	insertion_sort(A)
	print("after : " + str(A))

if __name__ == "__main__":
	main()