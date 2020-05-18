from math import floor

class heap:
	def __init__(self, A):
		self.A = A  # list holding a heap
		self.heap_size = len(A)

	def parent(self, i):
		return floor((i+1)/2)-1

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