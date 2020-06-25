# Recursion functions

# Factorial. For example factorial of 6 is 720. Looks like this: 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720


def factRecursice(number):
	if number == 1:  # for recursive method we must have BASE operation that stops from being stackoverflow
		return 1
	return number * factRecursice(number - 1)  # recursive method that goes until base operation is performed


def factIterative(number):
	result = 1  # in iterative method we will declare a variable which we need to return at the end
	for i in range(1, number + 1):  # in range of length of number as input including input number
		result *= i  # we multiple each number in that range each other
	return result  # returning final result


# print(factRecursice(6))  # printing results to console
# print(factIterative(6))  # printing results to console

# Fibonacci sequence

# Given a number N return the index value of the Fibonacci sequence, where sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each  value is the sum of the 2 previous values, that means that for
# N5 -> 2+3


def fibonacciIteretive1(n):   # time complexity is O(n)
	if n == 1 or n == 2:
		return 1
	a,b = 0,1
	for i in range(n):
		c = a + b  # declaring the variable to add first 2 numbers
		a = b      # a will become next item
		b = c      # b also will become next item which is sum of previous two numbers (c)
	return a       # will return a which is n stands


def fibonacciIteretive2(n):
	a = [0, 1]
	if n in a:
		return n
	for i in range(2, n+1):
		a.append(a[i-2] + a[i-1])
	return a[n]


def fibonacciRecursive(n):   # time complexity is O(n^2)
	if n < 2:
		return n
	return fibonacciRecursive(n-2)+fibonacciRecursive(n-1)


print(fibonacciIteretive1(35))
print(fibonacciIteretive2(35))
print(fibonacciRecursive(6))


def power_set(my_list):
	# base case: an empty list
	if len(my_list) == 0:
		return [[]]
	# recursive step: subsets without first element
	power_set_without_first = power_set(my_list[1:])
	# subsets with first element
	with_first = [[my_list[0]] + rest for rest in power_set_without_first]
	# return combination of the two
	return with_first + power_set_without_first


universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
	print(set)
