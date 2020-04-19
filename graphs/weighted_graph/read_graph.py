import sys
#sys.path.insert(1, '/Users/anton/programs/prep/graphs/weighted_graph/')
sys.path.insert(1, sys.path.insert(1, './'))
from graph import graph

def main():
	g = graph()
	g.read_from_file("basic_graph.tsv")
	g.calculate_adjacent()
	g.print_graph()

if __name__ == "__main__":
	main()