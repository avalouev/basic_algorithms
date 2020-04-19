from math import floor

def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	
	L = [0] * n1  # create empty arrays L, R
	R = [0] * n2
	L.append("*")  # sentinel
	R.append("*") 
	for i in range(n1):
		L[i] = A[p+i]
	for j in range(n2):
		R[j] = A[q+j+1]

	i = 0
	j = 0
	for k in range(p, r+1):
		if(L[i] <= R[j]):
			A[k] = L[i]
			i = i+1
		else:
			A[k] = R[j]
			j = j+1
	return

def test_merge():
	a = [10, 1, 3, 5, 2, 4, 6, 9]
	merge(A=a, p=1, q=3, r=6)
	assert(a == [10, 1, 2, 3, 4, 5, 6, 9])
	return

def merge_sort(A, p, r):
	if(p<r):
		q = int(floor((p+r)/2))
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)
	return

def test_merge_sort():
	a = [10, 4, 6, 8, 1, 3, 9, 2, 5, 5]
	merge_sort(a, 0, len(a)-1)
	assert(a == [1, 2, 3, 4, 5, 5, 6, 8, 9, 10])
	return

def test():
	test_merge()
	test_merge_sort()
	print("all tests passed")
	return

def main():
	test()
	
	a = [10, 4, 6 , 8, 1, 3, 9, 2, 5, 5]
	print("before sort - a: " + str(a))
	merge_sort(A=a, p=0, r=len(a) - 1)
	print("after sort - a : " + str(a))	

if __name__ == "__main__":
	main()