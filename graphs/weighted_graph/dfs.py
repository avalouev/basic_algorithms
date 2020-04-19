import sys
sys.path.insert(1, sys.path.insert(1, './'))
from graph import graph

def main():
	print("")
	g = graph()
	g.read_from_file("graph_Fig_22.4.tsv")
	g.print_graph()
	g.dfs(time=0)

if __name__ == "__main__":
	main()