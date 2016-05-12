'''
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from sympy import sieve
import itertools
import time

def doProblem():
	permPattern = '7654321'
	while True:	
		perms = list(map("".join, itertools.permutations(permPattern)))
		for p in perms:
			if int(p) in sieve:
				return p
		print('End of iterating 7654321')
		permPattern = '4321'

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
