import numpy as np

def int_max(x, y):
	if(x > y):
		return x
	return y

def knapsack(n=5, wt=[1, 2, 3], v=[60, 100, 120]):
	#print("Calculating knapsack")
	print("Knapsack size: " + str(n))
	for i in range(len(wt)):
		print("i: " + str(i) + " v: " + str(v[i]) + " w: " + str(v[i]))

	assert(len(wt) == len(v))

	max_value = -1  # tracks max value of knapsack

	M = np.zeros((len(wt)+1, n+1), dtype=int)  # knapsack value matrix
	for i in range(1, M.shape[0]):
		for j in range(1, M.shape[1]):
			val1 = 0
			if(wt[i-1] <= j):  # is current item weight < size of knapsack?
				val1 = v[i-1] + M[i-1, j - wt[i-1] ]
			val2 = M[i-1, j]
			M[i, j] = int_max(val1, val2)
			if(max_value < M[i, j]):
				max_value = M[i, j]
	print("")
	return max_value  # report maximum value of knapsack

def test_knapsack():
	value = knapsack(n=5, wt=[1, 2, 3], v=[60, 100, 120])
	assert(value == 220)

def main():
	test_knapsack()
	max_value = knapsack(n=7, wt=[1, 2, 3], v=[60, 100, 120])
	print("max value: " + str(max_value))

if __name__ == "__main__":
	main()