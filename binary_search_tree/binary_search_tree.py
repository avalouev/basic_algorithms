class binary_search_tree:
	def __init__(self):
		self.key = []  # node key
		self.left = [] # left child of a node
		self.right = [] # right child of a node
		self.p = [] # parent of a node
		self.root = -1 # index of the root

	def binary_search_tree_property(self):
		# varifies binary search tree property

		for ind, key in enumerate(self.key):
			left = self.left[ind]
			if(left != -1): # left child exists
				if self.key[left] <= key is False:
					return False
		return True

	def inorder_tree_walk(self, x):
		# implements Inorder-Tree-Walk(x) (page 255)

		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))
		assert(x < len(self.key))

		if(x >= 0):
			self.inorder_tree_walk(self.left[x])
			print(self.key[x])
			self.inorder_tree_walk(self.right[x])
		return

	def tree_search(self, x, k):
		# implements Tree-Search(x, k)		
		# given a pointer to the root x and a key k
		# searches for a node with that key (page 257)

		assert(x < len(self.key))
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))

		if(x < 0):
			return x
		if(k == self.key[x]):
			return x

		if(k < self.key[x]):
			return self.tree_search(self.left[x], k)
		else:
			return self.tree_search(self.right[x], k)

	def iterative_tree_search(self, x, k):
		# implements Iterative-Tree-Search(x, k) (page 257)

		assert(x < len(self.key))
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))

		while(x >= 0 and k!=self.key[x]):
			if(k < self.key[x]):
				x = self.left[x]
			else:
				x = self.right[x]
		return x

	def tree_minimum(self, x):
		# implements Tree-Minimum(x) (page 258)
		assert(x < len(self.key))
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))

		while(self.left[x] >= 0):
			x = self.left[x]
		return x

	def tree_maximum(self, x):
		# implements Tree-Maximum(x) (page 258)
		assert(x < len(self.key))
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))

		while(self.right[x] >= 0):
			x = self.right[x]
		return x

	def tree_successor(self, x):
		# implements Tree-Successor(x) (page 259)
		assert(x < len(self.key))
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))
		assert(len(self.key) == len(self.p))

		if(self.right[x] >= 0):
			return self.tree_minimum(self.right[x])
		y = self.p[x]
		while(y>=0 and x == self.right[y]):
			x = y
			y = self.p[y]
		return y

	def tree_insert(self, v):
		# implements Tree-Insert(T, z) (page 261)
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))
		assert(len(self.key) == len(self.p))
		assert(self.root >= 0)

		self.key.append(v)
		self.left.append(-1)
		self.right.append(-1)
		self.p.append(-1)
		z = len(self.key) - 1

		y = -1
		x = self.root
		while(x>=0):
			y = x
			if(self.key[z] < self.key[x]):
				x = self.left[x]
			else:
				x = self.right[x]

		self.p[z] = y
		if(y == -1):
			self.root = z
		else:
			if(self.key[z] < self.key[y]):
				self.left[y] = z
			else:
				self.right[y] = z
		return

	def tree_delete(self, z):
		# implements Tree-Delete(T, z) (page 262)
		assert(z < len(self.key))
		assert(len(self.key) == len(self.left))
		assert(len(self.key) == len(self.right))
		assert(len(self.key) == len(self.p))
		assert(self.root >= 0)

		if(self.left[z] == -1 or self.right[z] == -1):
			y = z
		else:
			y = self.tree_successor(z)

		if(self.left[y] != -1):
			x = self.left[y]
		else:
			x = self.right[y]

		if(x!=-1):
			self.p[x] = self.p[y]

		if(self.p[y] == -1):
			self.root = x
		else:
			if(y == self.left[self.p[y]]):
				self.left[self.p[y]] = x
			else:
				self.right[self.p[y]] = x

		if(y!=z):
			self.key[z] = self.key[y]

		return y
		return

def test():
	print("Running tests")
	print("-----------------")
	print("")

	print("Testing binary_search_tree_property")
	# define tree as in Figure 12.1 (page 254)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [5, 3, 7, 2, 5, 8]
	my_bs_tree.left = [1, 3, -1, -1, -1, -1]
	my_bs_tree.right = [2, 4, 5, -1, -1, -1]
	res = my_bs_tree.binary_search_tree_property()
	assert(res == True)

	print("Testing in_order_tree_walk")
	# define tree as in Figure 12.1 (page 254)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [5, 3, 7, 2, 5, 8]
	my_bs_tree.left = [1, 3, -1, -1, -1, -1]
	my_bs_tree.right = [2, 4, 5, -1, -1, -1]
	my_bs_tree.inorder_tree_walk(0)

	print("Testing tree_search")
	# evaluates the example in Figure 12.2 (page 257)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
	my_bs_tree.left = [1, 3, 5, 7, -1, -1, -1, -1, -1, 10, -1]
	my_bs_tree.right = [2, 4, 6, 8, 9, -1, -1, -1, -1, -1, -1]
	res = my_bs_tree.tree_search(0, 13) # start at root 0 and search for key 13
	assert(res == 9)

	print("Testing iterative_tree_search")
	# evaluates the example in Figure 12.2 (page 257)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
	my_bs_tree.left = [1, 3, 5, 7, -1, -1, -1, -1, -1, 10, -1]
	my_bs_tree.right = [2, 4, 6, 8, 9, -1, -1, -1, -1, -1, -1]
	res = my_bs_tree.iterative_tree_search(0, 13) # start at root 0 and search for key 13
	assert(res == 9)

	print("Testing tree_minimum")
	# evaluates the example in Figure 12.2 (page 257)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
	my_bs_tree.left = [1, 3, 5, 7, -1, -1, -1, -1, -1, 10, -1]
	my_bs_tree.right = [2, 4, 6, 8, 9, -1, -1, -1, -1, -1, -1]
	res = my_bs_tree.tree_minimum(0)
	assert(res == 7)

	print("Testing tree_maximum")
	# evaluates the example in Figure 12.2 (page 257)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
	my_bs_tree.left = [1, 3, 5, 7, -1, -1, -1, -1, -1, 10, -1]
	my_bs_tree.right = [2, 4, 6, 8, 9, -1, -1, -1, -1, -1, -1]
	res = my_bs_tree.tree_maximum(0)
	#print("res: " + str(res))
	assert(res == 6)

	print("Testing tree_successor")
	# evaluates the example in Figure 12.2 (page 257)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
	my_bs_tree.left = [1, 3, 5, 7, -1, -1, -1, -1, -1, 10, -1]
	my_bs_tree.right = [2, 4, 6, 8, 9, -1, -1, -1, -1, -1, -1]
	my_bs_tree.p = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 9]
	res = my_bs_tree.tree_successor(0)
	#print("res: " + str(res))
	assert(res == 5)	

	print("Testing tree_insert")
	# evaluates the example in Figure 12.3 (page 262)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key = [12, 5, 18, 2, 9, 15, 19, 17]
	my_bs_tree.left = [1, 3, 5, -1, -1, -1, -1, -1]
	my_bs_tree.right = [2, 4, 6, -1, -1, 7, -1, -1]
	my_bs_tree.p = [-1, 0, 0, 1, 1, 2, 2, 3]
	my_bs_tree.root = 0
	assert(my_bs_tree.binary_search_tree_property())
	my_bs_tree.tree_insert(13)
	assert(my_bs_tree.p == [-1, 0, 0, 1, 1, 2, 2, 3, 5])
	assert(my_bs_tree.left == [1, 3, 5, -1, -1, 8, -1, -1, -1])

	print("Testing tree_delete example 1")
	# evaluates the example in Figure 12.4.a (page 263)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key =   [15, 5, 16,  3, 12, 20, 10, 13, 18, 23,  6,  7]
	my_bs_tree.left =  [ 1, 3, -1, -1,  6,  8, 10, -1, -1, -1, -1, -1]
	my_bs_tree.right = [ 2, 4,  5, -1,  7,  9, -1, -1, -1, -1, -1, -1]
	my_bs_tree.p =     [ -1, 0, 0,  1,  1,  2,  4,  4,  5,  5,  6, 10]
	my_bs_tree.root = 0
	my_bs_tree.tree_delete(7)
	assert(my_bs_tree.right == [2, 4, 5, -1, -1, 9, -1, -1, -1, -1, -1, -1])

	print("Testing tree_delete example 2")
	# evaluates the example in Figure 12.4.b (page 263)
	my_bs_tree = binary_search_tree()
	my_bs_tree.key =   [15, 5, 16,  3, 12, 20, 10, 13, 18, 23,  6,  7]
	my_bs_tree.left =  [ 1, 3, -1, -1,  6,  8, 10, -1, -1, -1, -1, -1]
	my_bs_tree.right = [ 2, 4,  5, -1,  7,  9, -1, -1, -1, -1, -1, -1]
	my_bs_tree.p =     [ -1, 0, 0,  1,  1,  2,  4,  4,  5,  5,  6, 10]
	my_bs_tree.root = 0
	my_bs_tree.tree_delete(2)
	assert(my_bs_tree.right == [5, 4, 5, -1, 7, 9, -1, -1, -1, -1, -1, -1])

	print("-----------------")
	print("All tests passed")
	print("")


def main():
	test()

if __name__ == "__main__":
	main()