from math import floor

def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]

		i = j-1
		while(i >= 0 and A[i] > key):
			A[i + 1] = A[i]
			i = i-1
		A[i+1] = key

def bucket_sort(A):
	assert(len(A) > 0)
	max_el = A[0]
	for el in A:
		assert(el >= 0) 
		if(max_el < el):
			max_el = el

	A_normalized = [float(el) / float(max_el) for el in A]

	n = len(A_normalized)

	B = []  #  n buckets to be used for temp storage
	for i in range(n):
		empty_list = []
		B.append(empty_list)

	for i in range(n):
		B_ind = floor(n*A_normalized[i]) -1
		assert(B_ind < n)
		B[B_ind].append(A_normalized[i])

	for i in range(n):
		insertion_sort(B[i])

	A_sorted = []
	for i in range(len(B)):
		for j in range(len(B[i])):
			A_sorted.append(int(max_el*B[i][j]))
	return A_sorted

def main():
	a = [10, 4, 6 , 8, 1, 3, 9, 2, 5, 5]

	print("Before sorting: " + str(a))
	a_sorted = bucket_sort(a)
	print("After sorting:  " + str(a_sorted))

if __name__ == "__main__":
	main()