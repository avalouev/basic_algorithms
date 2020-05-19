from math import floor

class heap:
	def __init__(self, A):
		self.A = A  # list holding a heap
		self.heap_size = len(A)

	def parent(self, i):
		return int(floor((i+1)/2)-1)

	def left(self, i):
		return 2*(i+1) - 1

	def right(self, i):
		return 2*(i+1)

	def build_max_heap(self):
		# implements Build-Max-Heap(A) algorithm (page 133)
		
		for i in range(floor(len(self.A)/2), 0, -1):
			self.max_heapify(i-1)

	def max_heapify(self, i):
		# implements Max-Heapify(A, i) algorithm (page 130)

		l = self.left(i)
		r = self.right(i)

		largest = -1
		if(l < self.heap_size and self.A[l] > self.A[i]):
			largest = l
		else:
			largest = i

		if(r < self.heap_size and self.A[r] > self.A[largest]):
			largest = r

		if(largest != i):
			tmp = self.A[i]
			self.A[i] = self.A[largest]
			self.A[largest] = tmp
			self.max_heapify(largest)

	def heapsort(self):
		# implements Heapsort(A) algorithm (page 136)

		self.build_max_heap()

		for i in range(len(self.A), 1, -1):
			tmp = self.A[0]
			self.A[0] = self.A[i-1]
			self.A[i-1] = tmp
			self.heap_size -= 1
			self.max_heapify(0)

	def heap_extract_maximum(self):
		return self.A[0]

	def heap_extract_max(self):
		# implements Heap-Extract-Max(A) 
		# for max priority queue (page 139)

		if self.heap_size < 1:
			print("Error: heap underflow")
			return

		_max = self.A[0]
		self.A[0] = self.A[self.heap_size-1]
		self.heap_size -= 1
		self.max_heapify(0)
		return _max

	def heap_increase_key(self, i, key):
		# implements Heap-Increase-Key(A, i, key)
		# for max priority queue (page 140)

		if(key < self.A[i]):
			print("Error: new key is smaller than current key")
			return

		self.A[i] = key
		while(i > 0 and self.A[self.parent(i)] < self.A[i]):
			tmp = self.A[i]
			self.A[i] = self.A[self.parent(i)]
			self.A[self.parent(i)] = tmp
			i = self.parent(i)
		return

	def max_heap_insert(self, key):
		# implements Max-Heap-Insert(A, key) (page 140)
		# for max priority queue

		self.heap_size += 1
		if(len(self.A) < self.heap_size):
			self.A.append(key-1)
		else:
			self.A[self.heap_size-1] = key-1
		self.heap_increase_key(self.heap_size-1, key)

	def build_max_heap_prime(self):
		# implements Build-Max-Heap'(A) (page 142)

		self.heap_size = 1
		for i in range(1, len(self.A)):
			self.max_heap_insert(self.A[i])

	def validate_max_heap(self):
		# validates if max heap property is true

		for i in range(self.heap_size-1, 0, -1):
			if(self.A[self.parent(i)] < self.A[i]):
				print("Max heap property failed")
				return False
		return True




