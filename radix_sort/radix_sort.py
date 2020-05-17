def get_digits(n, mod=10):
	# returns a list containing digits of the number n
	res = []

	nmod_prev = n
	i = 1

	while(nmod_prev != 0):
		remainder = int(nmod_prev % mod)
		res = [remainder] + res
		nmod_prev = int((nmod_prev - remainder) / mod)
		i += 1

	return res

def pad_digits(a_digits):
	# takes a list of numbers represented as digits
	# and pads them with 0s in front
	# returns a list of digits padded to the same length

	assert(len(a_digits) > 0)

	max_len = len(a_digits[0])
	for i in range(1, len(a_digits)):
		if(max_len < len(a_digits[i])):
			max_len = len(a_digits[i])

	a_digits_padded = []

	for i in range(len(a_digits)):
		cur_a = a_digits[i]
		for j in range(max_len - len(a_digits[i])):
			cur_a = [0] + cur_a

		a_digits_padded.append(cur_a)

	return a_digits_padded, max_len

def stable_insertion_sort_on_digits(A, ind):
	assert(len(A) > 0)
	assert(ind < len(A[0]))
	for j in range(1, len(A)):
		key_arr = A[j]
		key = A[j][ind]
		i = j-1
		while(i >= 0 and A[i][ind] > key):
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key_arr

def radix_sort_on_digit(A, d):
	# implements textbook radix sort
	# A - a list of input numbers, each represented by 
	# a list of digits, padded in front to the same length
	# d - number of digits, i.e. length of each list of digits for each number in A

	# returns a radix-sorted list of digits

	for i in range(0, d):
		stable_insertion_sort_on_digits(A, d-i-1)

def digits_to_numbers(A, mod):
	# converts digits to numbers
	res = []
	for i in range(len(A)):
		digits = A[i]
		cur_num = 0
		for j in range(len(digits)):
			cur_num += digits[len(digits)-j-1] * pow(mod, j) #mod^j
		res.append(cur_num)

	return res

def radix_sort(a, mod=10):

	for i in range(len(a)):
		assert(a[i] > 0)
		assert(int(a[i]) == a[i])

	a_digits = [get_digits(el, mod) for el in a]
	a_digits_padded, d = pad_digits(a_digits)
	radix_sort_on_digit(a_digits_padded, d)
	a_sorted = digits_to_numbers(a_digits_padded, mod)

	return a_sorted

def test():
	print("Running tests")
	a = [329, 457, 657, 839, 436, 720, 355]
	a_sorted = radix_sort(a)
	assert(a_sorted == [329, 355, 436, 457, 657, 720, 839])
	print("All tests passed")
	print("")

def main():

	test()
	a = [10, 4, 6 , 108, 1, 3, 99, 203, 5, 5, 10001]

	print("Before sorting: " + str(a))

	a_sorted = radix_sort(a)

	print("After sorting: " + str(a_sorted))

if __name__ == "__main__":
	main()