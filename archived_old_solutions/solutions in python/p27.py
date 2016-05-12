#coding: utf-8

'''
Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

'''
from sympy import sieve
import time

def PrimeList1to1000():
	return sieve.primerange(1,1001)

def OddList1to1000():
	pool = []
	for i in range(500):
		pool.append(i*2+1)
	return pool

def CheckPrimesLength(a,b):
	n = 0
	while ((n*n+a*n+b) in sieve):
		n+=1
	return n

def DoProblem():
	max = 0
	max_a = 0
	max_b = 0
	for b in PrimeList1to1000():
		for a in OddList1to1000():
			na = (-1)*a
			if CheckPrimesLength(na,b) > max:
				max = CheckPrimesLength(na,b)
				max_a = na
				max_b = b
			
	return (max_a,max_b,max,max_a*max_b)

print('start')
start = time.time()
print(DoProblem())
print(time.time()-start)
