
def push(S, x):
	S.append(x)

def pop(S):
	if(len(S) > 0):
		del S[-1]
	return

def stack_empty(S):
	if(len(S) > 0):
		return False
	return True

def test_push():
	S = [1, 2, 3]
	push(S, 4)
	assert(S == [1,2,3,4])

def test_pop():
	S = [1, 2, 3]
	pop(S)
	assert(S == [1, 2])

def test_stack_empty():
	S  = [1, 2]
	pop(S)
	pop(S)
	assert( S == [])

def test_stack():
	test_push()
	test_pop()
	test_stack_empty()

def main():
	print("Executing main")

	# testing 
	test_stack()

	S = [10, 20, 30]
	push(S, 40)
	print("S: " + str(S))
	pop(S)
	print("S: " + str(S))

	while not stack_empty(S):
		pop(S)

	print("S: " + str(S))

	return

if __name__ == "__main__":
	main()