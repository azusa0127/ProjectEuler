'''
Problem 35: Circular primes
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and
719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''
import time
from sympy import sieve

def RotateNumSet(n):
	nSet = set()
	nSet.add(n)
	tmp = str(n)[-1:] + str(n)[:-1]
	while (tmp != str(n)):
		nSet.add(int(tmp))
		tmp = tmp[-1:] + tmp[:-1]
	return nSet

def CircularCheck(n):
	for rnum in RotateNumSet(n):
		if rnum not in sieve:
			return False 
	return True 
	
def GenerateCPrimeSet(limit):
	solSet = set()
	for i in sieve.primerange(1,limit):
		if i not in solSet:
			if CircularCheck(i):
				solSet.update(RotateNumSet(i))
	return solSet

print('start')
start = time.time()
print(len(GenerateCPrimeSet(1000000)))
print('end')
print(time.time()-start)
