import sys
sys.path.insert(1, sys.path.insert(1, './'))
from graph import graph

def main():
	g = graph()
	g.read_from_file("graph_Fig_24.4.tsv")
	g.print_graph()
	res = g.bellman_ford("s")
	print("res: " + str(res))

if __name__ == "__main__":
	main()