
# dynamic programming is just fancy way of saying optimizing code for not repeating ourself.
# for example on this function we get n number added to 80
def addto80(n):
	print('long time')
	return n+80

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










