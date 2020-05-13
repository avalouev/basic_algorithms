def counting_sort(A, B, k):
	assert(len(A) == len(B)) # input and sorted output sizes match

	# init temp list for working storage
	C = [0] * k
	for j in range(len(A)):
		C[A[j]] = C[A[j]] + 1
	# C now contains the number of elements equal to i+1

	for i in range(k):
		C[i] = C[i] + C[i-1]
	# C now contains the number of elements less than or equal to i+1

	# sort elements
	for j in range(len(A)-1, -1, -1):
		assert(C[A[j]]-1 < len(B)) # increase k if this fails
		B[C[A[j]]-1] = A[j]
		C[A[j]] = C[A[j]] -1

	return

def main():
	a = [10, 4, 6 , 8, 1, 3, 9, 2, 5, 5, 1000]

	assert(len(a) > 0)
	sorted_a = [0] * len(a) # create placeholder for sorted list

	for i in range(len(a)):
		assert(a[i] >= 0)

	max_a = a[0]
	for i in range(len(a)):
		if(max_a < a[i]):
			max_a = a[i]

	assert(max_a < 10000) # too much memory would be required otherwise

	print("Before sorting: " + str(a))
	counting_sort(a, sorted_a, max_a+2)
	print("After sorting:  " + str(sorted_a))

if __name__ == "__main__":
	main()