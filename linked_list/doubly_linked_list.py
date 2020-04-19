import numpy as np

_free = -1 # top of the free memory list

class doubly_linked_list:
	_size = 0  # array size to hold the data structure
	_next = None
	_key = None
	_prev = None
	_head = None

	free_next = None  # singly linked list for free memory

	def __init__(self):
		global _free
		print("constructing list")
		self._size = 10
		self._next = np.full((self._size), -1, dtype = int)
		self._key = np.full((self._size), -1, dtype = int)
		self._prev = np.full((self._size), -1, dtype = int)
		self._head = -1
		self.free_next = np.arange(1, self._size + 1)
		self.free_next[self._size-1] = -1
		_free = 0

	def raw_print(self):
		for i in range(self._size):
			if(self._head == i):
				print("i=" + str(i) + ": [" + str(self._next[i]) + ", " + 
					str(self._key[i]) + ", " + str(self._prev[i]) + "] *")
			else:
				print("i=" + str(i) + ": [" + str(self._next[i]) + ", " + 
					str(self._key[i]) + ", " + str(self._prev[i]) + "]")

	def allocate(self):
		global _free
		if _free == -1:
			print("Out of space")
			return -1

		x = _free
		_free = self.free_next[x]
		return x

	def free_object(self, x):
		global _free
		self.free_next[x] = _free
		_free = x
		self._next[x] = -1
		self._key[x] = -1
		self._prev[x] = -1

	def search(self, k):
		if(self._head == -1):
			print("Failed search - list empty")
			return -1
		
		x = self._head
		continue_traverse = True

		while continue_traverse:
			if(self._key[x] == k):
				continue_traverse = False
				#print("Found " + str(k) + " at ptr=" + str(x))
				return x
			
			if(self._next[x] == -1) :
				continue_traverse = False
				return -1

			x = self._next[x]

	def insert(self, x):
		new_ptr = self.allocate()
		print("insert new_ptr: " + str(new_ptr))
		if(self._head == -1):
			print("empty")
			self._head = new_ptr
			self._prev[new_ptr] = -1
			self._next[new_ptr] = -1
		else:
			self._prev[self._head] = new_ptr
			self._next[new_ptr] = self._head

		#self._prev[self._head] = new_ptr
		self._key[new_ptr] = x

		self._head = new_ptr
		self._prev[new_ptr] = -1

	def delete(self, k):
		x = self.search(k)
		print("Delete " + str(k))
		if(x == -1):
			print("Element not found")
			return  # no element to be deleted
		print("Found match @ ptr=" + str(x))

		if(self._prev[x] != -1):
			self._next[self._prev[x]] = self._next[x]
		else:
			self._head = self._next[x]
		if(self._next[x] != -1):
			self._prev[self._next[x]] = self._prev[x]

		self.free_object(x)

def main():
	print("Executing main")
	L = doubly_linked_list()
	L.raw_print()
	
	L.insert(10)
	print("")
	L.raw_print()

	L.insert(20)
	print("")
	L.raw_print()

	L.insert(20)
	print("")
	L.raw_print()

	L.insert(30)
	print("")
	L.raw_print()
	print("")

	#L.search(10)
	#print("")
	L.delete(20)

	print("")
	L.raw_print()

	L.insert(40)
	print("")
	L.raw_print()

	L.delete(20)
	print("")
	L.raw_print()

	L.insert(50)
	print("")
	L.raw_print()



if __name__ == "__main__":
	main()