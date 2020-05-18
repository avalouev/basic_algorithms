#import heap as heap
from heap import heap

def test_max_heap():
	print("Running tests")
	print("-------------")
	a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
	my_heap = heap(a)	

	print("Testing parents, left, right")
	assert(my_heap.parent(1) == 0)
	assert(my_heap.parent(2) == 0)
	assert(my_heap.left(0) == 1)
	assert(my_heap.right(0) == 2)

	print("Testing max_heapify")
	# Test behavior as in Figure 6.2 (page 131)
	a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
	my_heap = heap(a)
	my_heap.max_heapify(1)
	assert(my_heap.A == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

	print("Testing build_max_heap")
	# Test behavior as in Figure 6.3 (page 134)
	a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	my_heap = heap(a)
	my_heap.build_max_heap()
	assert(my_heap.A == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

	print("Testing heapsort")
	a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
	my_heap = heap(a)
	my_heap.heapsort()
	assert(my_heap.A == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])

	print("-------------")
	print("All tests passed")
	print("")

def heapsort(a):
	my_heap = heap(a)
	my_heap.heapsort()
	a = my_heap.A

def main():
	test_max_heap()

	a = [10, 4, 6 , 108, 1, 3, 99, 203, 5, 5, 10001]

	print("Before sort: " + str(a))
	heapsort(a)
	print("After sort:  " + str(a))

if __name__ == "__main__":
	main()