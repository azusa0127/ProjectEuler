#coding: utf-8
'''
Problem 47: Distinct primes factors
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors. What is the first
of these numbers?
'''
from sympy.ntheory import primefactors
import time

def lengthOfPrimeFacs(n):
	return len(primefactors(n))

def doProblem():
	n = 647
	while True:
		if lengthOfPrimeFacs(n) != 4:
			n += 4
			continue 
		elif lengthOfPrimeFacs(n-2) == 4:
			if lengthOfPrimeFacs(n-1) == 4:
				if lengthOfPrimeFacs(n-3) == 4:
					return n-3
				elif lengthOfPrimeFacs(n+1) == 4:
					return n-2
				else:
					n += 5
			else: 
				n += 3
				continue 
		n += 2

print('start')
start = time.time()
print(doProblem())
print('end')
print(time.time()-start)
