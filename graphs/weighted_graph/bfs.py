import sys
sys.path.insert(1, sys.path.insert(1, './'))
from graph import graph

def main():
	print("")
	g = graph()
	g.read_from_file("graph_Fig_22.3.tsv")
	g.print_graph()
	g.bfs("s")
	g.print_path("w", "u")

if __name__ == "__main__":
	main()