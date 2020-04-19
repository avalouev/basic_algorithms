def enqueue(Q, x):
	Q.append(x)

def dequeue(Q):
	res = Q[0]
	del Q[0]
	return res

def test_enqueue():
	Q = [1, 2]
	enqueue(Q, 3)
	assert(Q == [1, 2, 3])

def test_dequeue():
	Q = [1, 2, 3]
	dequeue(Q)
	assert(Q == [2, 3])

def test_queue():
	test_enqueue()
	test_dequeue()

def main():
	test_queue()

	Q = [10, 20, 30]
	print("Q: " + str(Q))
	enqueue(Q, 40)
	print("Q: " + str(Q))
	dequeue(Q)
	print("Q: " + str(Q))
	print("Executing main")

if __name__ == "__main__":
	main()