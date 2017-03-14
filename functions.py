def ptint_spam ():
	print ('spam\n' * 3)

#ptint_spam ()

def pow_of_two (number):
	print (number ** 2)

#pow_of_two (12)

def maxi (x, y):
	if x > y:
		return x
	else:
		return y

#print (maxi ('test', 'tesa'))

def fib (n):
	f = [0, 1]
	for i in range (2, n+1):
		f.append (f[i-1] + f[i-2])
	print (f)

n = input('fibon count: ')
fib(int(n))