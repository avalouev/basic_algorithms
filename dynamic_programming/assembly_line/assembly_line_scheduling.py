class assembly_line:
	def __init__(self):
		# declare assembly line variables
		self.set_to_none()

	def set_to_none(self):
		self.a = None
		self.t = None
		self.e = None
		self.x = None
		self.n = None
		self.f = None
		self.l = None

		self.f_star = None
		self.l_star = None

	def test(self):

		print("Running tests")

		print("Init example assembly line")
		self.e = [2, 4]
		self.a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
		self.t = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
		self.x = [3, 2]
		self.n = 6

		print("Test variable diminesions")
		self.test_variables()

		print("Test correctness of solution")
		self.fastest_way()
		assert(self.f_star == 38)
		assert(self.l_star == 0)
		assert(self.f[0] == [9, 18, 20, 24, 32, 35])
		assert(self.f[1] == [12, 16, 22, 25, 30, 37])
		assert(self.l[0] == [0, 0, 1, 0, 0, 1])
		assert(self.l[1] == [0, 0, 1, 0, 1, 1])

		#self.print()

		print("All tests passed")

	def test_variables(self):
		assert(len(self.e) == 2)
		assert(len(self.a) == 2)
		assert(len(self.a[0]) == len(self.a[1]))
		assert(len(self.a[0]) == self.n)
		assert(len(self.t) == 2)
		assert(len(self.t[0]) == len(self.t[1]))
		assert(len(self.t[0]) == self.n-1)
		assert(len(self.x) == 2)

	def print(self):
		print("a: ")
		print(self.a[0])
		print(self.a[1])
		print("")

		print("t: ")
		print(self.t[0])
		print(self.t[1])
		print("")

		print("f:")
		print(self.f[0])
		print(self.f[1])
		print("")

		print("l:")
		print(self.l[0])
		print(self.l[1])
		print("")
	
		print("f_star: " + str(self.f_star))
		print("l_star: " + str(self.l_star))
		print("")

	def fastest_way(self): 
		# implements Fastest-Way(a, t, e, x, n) from page 329

		# init dummy variable f for the fastest time
		self.f = []
		self.f.append([0] * self.n)
		self.f.append([0] * self.n)

		# define dummy line number variable to keep track of 
		# the fastest path through the assembly line
		self.l = []
		self.l.append([0] * self.n)
		self.l.append([0] * self.n)

		#print(f)
		self.f[0][0] = self.e[0] + self.a[0][0]
		self.f[1][0] = self.e[1] + self.a[1][0]

		# init final values:
		# f_star (fastest time after n steps)
		# l_star (last line after n steps)

		self.f_star = -1
		self.l_star = -1

		for j in range(1, self.n):
			#  optimal solution: 
			#  f[0][j] = max(f[0][j-1] + a[0][j], [1][j-1] + t[1][j-1] + a[0][j])

			if(self.f[0][j-1] + self.a[0][j] <= \
				self.f[1][j-1] + self.t[1][j-1] + self.a[0][j]):
				self.f[0][j] = self.f[0][j-1] + self.a[0][j]
				self.l[0][j] = 0
			else:
				self.f[0][j] = self.f[1][j-1] + self.t[1][j-1] + self.a[0][j]
				self.l[0][j] = 1

			#  optimal solution: 
			#  f[1][j] = max(f[1][j-1] + a[1][j], f[1][j-1] + t[0][j-1] + a[1][j])

			if(self.f[1][j-1] + self.a[1][j] <= \
				self.f[0][j-1] + self.t[0][j-1] + self.a[1][j]):
				self.f[1][j] = self.f[1][j-1] + self.a[1][j]
				self.l[1][j] = 1
			else:
				self.f[1][j] = self.f[0][j-1] + self.t[0][j-1] + self.a[1][j]
				self.l[1][j] = 0

		if(self.f[0][self.n-1] + self.x[0] <= self.f[1][self.n-1] + self.x[1]):
			self.f_star = self.f[0][self.n-1] + self.x[0]
			self.l_star = 0
		else:
			self.f_star = self.f[1][self.n-1] + self.x[1]
			self.l_star = 1

	def print_stations(self):
		# implements Print-Stations(l, n) as on page 330
		i = self.l_star
		print("line " + str(i) + ", station " + str(self.n-1))

		for j in range(self.n-1, 0, -1):
			i = self.l[i][j]
			print("line " + str(i) + ", station " + str(j-1))

		print("")

def main():
	print("Printing from main")

	# define assembly line as in Fig. 15.2 (page 326)

	my_assembly_line = assembly_line()
	my_assembly_line.test()

	my_assembly_line.e = [2, 4]
	my_assembly_line.a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
	my_assembly_line.t = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
	my_assembly_line.x = [3, 2]
	my_assembly_line.n = 6

	my_assembly_line.fastest_way()
	my_assembly_line.print()
	my_assembly_line.print_stations()

if __name__ == "__main__":
	main()