#coding: utf-8
'''
Goldbach's other conjecture
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from sympy import sieve
import time

def CheckGConjecture(n):
	for i in sieve.primerange(1,n):
		if ((n-i)/2)**0.5 == int(((n-i)/2)**0.5):
			return True
	return False

def doProblem():
	n = 33
	while True :
		n += 2
		if n not in sieve:
			if CheckGConjecture(n) == False:
				return n
		
print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
