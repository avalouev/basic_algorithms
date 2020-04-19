
class vertex:
	def __init__(self, key):
		#print("Vertex constructor")
		#print("Add vertex: " + str(key))
		self.key = key
		self.neighbors = [] # for directed edges
		self.weights = []
		self.adj = [] # keep track of all adjacent edges regardles direction
		return

