'''
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''
import time
from math import sqrt

print('start')
start = time.time()

def SumProperDivisors(n):
	sum = 0
	limit = int(sqrt(n))
	for i in range(1,limit+1):
		if (i*i==n):
			sum += i
		elif (n%i==0):
			sum += i + (n/i)
	sum -= n
	return sum

def IfAbundantNum(n):
	if (SumProperDivisors(n)>n):
		return True
	else: 
		return False

def BuildANList():
	list = []
	for i in range(12,28124):
		if IfAbundantNum(i):
			list.append(i)
	return list

anlist = BuildANList()
anset = set(anlist)

def CheckIfAbundantSum(n):
	for i in anlist:
		if (i > n):
			return False
		if (n-i) in anset:
			return True
	return False

def SumAllNonAbundantNums():
	sum = 0 
	for i in range(1,28124):
		if (CheckIfAbundantSum(i) == False):
			sum += i
	return sum

print(SumAllNonAbundantNums())
print('end')
print(time.time()-start)

