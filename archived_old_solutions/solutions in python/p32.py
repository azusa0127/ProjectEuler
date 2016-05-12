#coding: utf-8
'''
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as
a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your
sum.
'''
from sets import Set
import time

def IsPandigital(strn):
	if sorted(strn) == ['1','2','3','4','5','6','7','8','9']:
		return True 
	return False 

def IterMultiplicand():
	solSet = set()
	for i in range(1234,98765+1):
		for j in range(1,len(str(i))):
			num = str(i) + str(int(str(i)[:j]) * int(str(i)[j:]))
			if IsPandigital(num):
				solSet.add(int(str(i)[:j]) * int(str(i)[j:]))
	return solSet

def SumTheSet(_set):
	sum = 0
	for v in _set:
		sum += v
	return sum

print('start')
start = time.time()
print(SumTheSet(IterMultiplicand()))
print('end')
print(time.time()-start)
