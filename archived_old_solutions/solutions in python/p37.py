'''
Problem 37: Truncatable primes
The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right
to left.
'''
import time
from sympy import sieve
from sympy import nextprime

def TruncatableTest(n):
	tmp = str(n)
	while len(tmp)>1:
		 tmp = tmp[1:]
		 if int(tmp) not in sieve:
		 	return False 
	tmp = str(n)
	while len(tmp)>1:
		tmp = tmp[:-1]
		if int(tmp) not in sieve:
			return False
	return True
	
def doProblem():
	count = 0
	sum = 0
	i=10
	while count < 11:
		i = nextprime(i)
		if TruncatableTest(i):
#			print(i)
			sum += i
			count += 1
	return sum
			
print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
