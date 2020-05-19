import sys
sys.path.insert(1, './../heap/')

from heap import heap

def test():
	print("Running tests")
	print("-------------")

	# test extract max
	print("Testing heap extract max")
	a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
	my_heap = heap(a)
	heap_max = my_heap.heap_extract_max()
	assert(my_heap.A == [14, 8, 10, 4, 7, 9, 3, 2, 1, 1])

	# test increase key (as in Fig. 6.5 on page 141)
	print("Testing heap increase key")
	a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
	my_heap = heap(a)
	my_heap.heap_increase_key(8, 15) #(5, 17) #(3, 15)
	assert(my_heap.A == [16, 15, 10, 14, 7, 9, 3, 2, 8, 1])

	# test max heap insert
	print("Testing max heap insert")
	a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
	my_heap = heap(a)
	my_heap.max_heap_insert(5) #(5, 17) #(3, 15)
	assert(my_heap.A == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 5])

	# test build max heap prime
	print("Testing build max heap prime")
	a = [2, 7, 4, 1, 16, 10, 9, 3, 14, 8]
	my_heap = heap(a)
	my_heap.build_max_heap_prime()
	res = my_heap.validate_max_heap()
	assert(res == True)
	assert(my_heap.A == [16, 14, 10, 7, 8, 4, 9, 1, 3, 2])

	print("-------------")
	print("All tests passed")
	print("")

def main():
	test()

if __name__ == "__main__":
	main()