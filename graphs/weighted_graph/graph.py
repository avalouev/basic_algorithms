from vertex import vertex
import csv

import sys
sys.path.insert(1, './../../queue/')

from queue import enqueue, dequeue

class graph:

	def __init__(self):
		self.vertices = []
		self.vertex_names = []
		return

	def read_from_file(self, file_name):
		with open(file_name, 'r') as csvfile:
			graph_reader = csv.reader(csvfile, delimiter='\t', quotechar='|')			
			for row in graph_reader:
				assert(len(row) == 3)
				from_vertex = row[0]
				to_vertex = row[1]
				weight = float(row[2])

				# create vertex objects
				if from_vertex not in self.vertex_names:
					self.vertex_names.append(from_vertex)
					new_vertex = vertex(from_vertex)
					new_vertex.neighbors.append(to_vertex)
					new_vertex.weights.append(weight)
					self.vertices.append(new_vertex)
				else:
					ind = self.vertex_names.index(from_vertex)
					if to_vertex not in self.vertices[ind].neighbors:
						self.vertices[ind].neighbors.append(to_vertex)
						self.vertices[ind].weights.append(weight)
						x=0
					else:
						print("Skipping duplicate edge: " + str(from_vertex) + " -> " + 
							str(to_vertex) + " w: " + str(weight))

				if to_vertex not in self.vertex_names:
					self.vertex_names.append(to_vertex)
					new_vertex = vertex(to_vertex)
					self.vertices.append(new_vertex)
			self.calculate_adjacent()
		return

	def calculate_adjacent(self):
		# go through the list of vertices and calculate adjacency list
		for i, from_v in enumerate(self.vertex_names):
			assert(from_v == self.vertices[i].key)
			for j, to_v in enumerate(self.vertices[i].neighbors):
				if to_v not in self.vertices[i].adj:
					self.vertices[i].adj.append(to_v)
				to_ind = self.vertex_names.index(to_v)
				assert(to_ind >= 0)
				if from_v not in self.vertices[to_ind].neighbors:
					self.vertices[to_ind].adj.append(from_v)

	def bfs(self, s):
		# breadth first search
		print("From bfs(self, s):")
		assert(s in self.vertex_names)
		s_ind = self.vertex_names.index(s)

		self.color = ["NIL"] * len(self.vertex_names)
		self.d = [-1] * len(self.vertex_names)
		self.pi = ["NIL"] * len(self.vertex_names)

		for i, u in enumerate(self.vertex_names):
			if(u != s):
				self.color[i] = "WHITE"
				self.d[i] = -1 # instead of inf
				self.pi[i] = "NIL"

		self.color[s_ind] = "GRAY"
		self.d[s_ind] = 0
		self.pi[s_ind] = "NIL"
		Q = []
		enqueue(Q, s)

		while(len(Q) != 0):
			u = dequeue(Q)
			u_ind = self.vertex_names.index(u)
			for v in self.vertices[u_ind].adj:
				v_ind = self.vertex_names.index(v)
				if(self.color[v_ind] == "WHITE"):
					self.color[v_ind] = "GREY"
					self.d[v_ind] = self.d[u_ind] + 1
					self.pi[v_ind] = u
					enqueue(Q, v)
			self.color[u_ind] = "BLACK"

		for i, v in enumerate(self.vertex_names):
			print("v: " + str(v) + " d: " + str(self.d[i]) + " p: " + str(self.pi[i]))
		print("")

	def print_path(self, s, v):
		# prints out vertices on a shortest path from s to v, 
		# assuming that BFS has already been run to computer shortest 
		# path tree
		if (v==s):
			print(s)
		else:
			v_ind = self.vertex_names.index(v)
			if(self.pi[v_ind] == "NIL"):
				print("no path from " + s + " to " + v + " exists")
			else:
				self.print_path(s, self.pi[v_ind])
				print(v)
		return

	def dfs_visit(self, u, time):
		u_ind = self.vertex_names.index(u)		
		self.color[u_ind] = "GRAY" # White vertex u has just been discovered
		time = time + 1
		self.d[u_ind] = time

		for v in self.vertices[u_ind].neighbors:
			v_ind = self.vertex_names.index(v)
			if(self.color[v_ind] == "WHITE"):
				self.pi[v_ind] = u
				time = self.dfs_visit(v, time)
		
		self.color[u_ind] = "BLACK" # Black u; it is finished.
		time = time + 1
		self.f[u_ind] = time
		return time


	def dfs(self, time):
		#global time
		self.color = ["WHITE"] * len(self.vertex_names)
		self.pi = ["NIL"] * len(self.vertex_names)
		self.d = [-1] * len(self.vertex_names)
		self.f = [-1] * len(self.vertex_names)

		for u_ind, u in enumerate(self.vertex_names):
			if(self.color[u_ind] == "WHITE"):
				time = self.dfs_visit(u, time)

		print("DFS done")
		for v_ind, v in enumerate(self.vertex_names):
			print(v + ": d: " + str(self.d[v_ind]) + " f: " + 
				str(self.f[v_ind]))
		print("")
		return

	def initialize_single_source(self, s):
		self.d = [0] * len(self.vertex_names)
		self.d_inf = [True] * len(self.vertex_names) # initial dist is inf
		self.pi = ["NIL"] * len(self.vertex_names)

		s_ind = self.vertex_names.index(s)
		self.d[s_ind] = 0
		self.d_inf[s_ind] = False
		return

	def get_directed_edges(self):
		edges = []
		for u_ind, u in enumerate(self.vertex_names):
			for v_ind, v in enumerate(self.vertices[u_ind].neighbors):
				weight = self.vertices[u_ind].weights[v_ind]
				cur_edge = [u, v, weight]
				edges.append(cur_edge)
		return edges

	def relax(self, u, v, w):
		u_ind = self.vertex_names.index(u)
		v_ind = self.vertex_names.index(v)
		assert(self.d_inf[u_ind] == False)
		if(self.d_inf[v_ind] == True):
			self.d[v_ind] = self.d[u_ind] + w
			self.pi[v_ind] = u
			self.d_inf[v_ind] = False
		else:
			if(self.d[v_ind] > self.d[u_ind] + w):
				self.d[v_ind] = self.d[u_ind] + w
				self.pi[v_ind] = u
		return

	def bellman_ford(self, s):
		self.initialize_single_source(s)
		edges = self.get_directed_edges()

		for i in range(len(self.vertex_names)):
			for edge in edges:
				self.relax(edge[0], edge[1], edge[2])

		for edge in edges:
			u = edge[0]
			u_ind = self.vertex_names.index(u)
			v = edge[1]
			v_ind = self.vertex_names.index(v)
			w = edge[2]
			if(self.d[v_ind] >  self.d[u_ind] + w):
				return False

		for v_ind, v in enumerate(self.vertex_names):
			print(v + ", d: " + str(self.d[v_ind]))
		print("")
		return True

	def print_graph(self):
		print("printing directed graph: ")
		for i in range(len(self.vertices)):
			print(self.vertices[i].key + ": n: " + 
				str(self.vertices[i].neighbors) + " w: " + str(self.vertices[i].weights))

		print("")
		print("printing adjacency list")
		for i in range(len(self.vertices)):
			v_ind = self.vertex_names.index(self.vertices[i].key)
			print(self.vertices[i].key + " ind: " + str(v_ind) + 
				" : adj: " +  str(self.vertices[i].adj))
		print("")

