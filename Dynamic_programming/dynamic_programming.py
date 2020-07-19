# dynamic programming is just fancy way of saying optimizing code for not repeating ourself.
# for example on this function we get n number added to 80
def addto80(n):
	print('long time')
	return n + 80


print(addto80(10))
print(addto80(10))
print(addto80(10))
print(addto80(10))
# when we call it with any number it returns number +80. but when we call it with same number
# process goes all over and it calculates and returns. for big operations it can be costly.
# that's why dynamic programming can be handy.
cashe = {}


def memoizedaddto80(n):
	if n in cashe:
		return cashe[n]
	else:
		print('long time')
		cashe[n] = n + 80
		return cashe[n]


print(memoizedaddto80(10))
print(memoizedaddto80(10))
print(memoizedaddto80(10))
print(memoizedaddto80(10))


# in above function stores calculation in cashe and returns item if requested number previously calculated.
# with this way we can skip calculation and return requested result fast.


# another example is fibonacci


def fib(n):
	if n < 2:
		return n
	return fib(n - 1) + fib(n - 2)


def fibonaccimaster(n):
	if n< 2:
		return n
	a, b = 0, 1
	for i in range(n):
		c = a+b
		a = b
		b = c
	return a


def fib2(n):
	sum_numbers = [0, 1]
	for i in range(2, n+1):
		sum_numbers.append(sum_numbers[i-2]+sum_numbers[i-1])
	return sum_numbers.pop()

print(fib(35))
print(fibonaccimaster(35))
print(fib2(35))
